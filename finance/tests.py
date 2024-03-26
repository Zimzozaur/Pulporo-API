from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.db.models import PROTECT, CASCADE, SET_NULL
import datetime
from .models import Company, CashTag, Currency, OneIO
from .views import ReadIO



# ---------- Views ----------
class ReadIOView(TestCase):
    fixtures = ['ReadIO.json']
    this_month = datetime.date.today().replace(day=1)
    last_month = this_month - datetime.timedelta(days=1)

    @classmethod
    def setUpClass(cls):

        fixture_path = 'finance/fixtures/ReadIO.json'
        template_fixture = 'finance/fixtures/ReadIO_template.json'

        Currency.objects.create()
        User.objects.create()

        with open(template_fixture, 'r') as f:
            f_data = f.read()
            f_data = f_data.replace("__CURRENT_MONTH__", str(ReadIOView.this_month))
            f_data = f_data.replace("__LAST_MONTH__", str(ReadIOView.last_month))
        with open(fixture_path, 'w') as f:
            f.write(f_data)
        super().setUpClass()

    def setUp(self):
        self.r = RequestFactory()
        self.this = ReadIOView.this_month
        self.last = ReadIOView.last_month

    def test_this_month_outcome(self):
        r = self.r.get('/')
        view = ReadIO()
        view.request = r
        qs = view.get_queryset()
        self.assertEqual(50, qs[0].value)

    def test_this_month_income(self):
        r = self.r.get('/', {
            'chosen_year': self.this.year,
            'chosen_month': self.this.month,
            'is_outcome': False
        })
        view = ReadIO()
        view.request = r
        qs = view.get_queryset()
        self.assertEqual(100, qs[0].value)

    def test_last_month_outcome(self):
        r = self.r.get('/', {
            'chosen_year': self.last.year,
            'chosen_month': self.last.month,
            'is_outcome': True
        })
        view = ReadIO()
        view.request = r
        qs = view.get_queryset()
        self.assertEqual(90, qs[0].value)

    def test_last_month_income(self):
        r = self.r.get('/', {
            'chosen_year': self.last.year,
            'chosen_month': self.last.month,
            'is_outcome': False
        })
        view = ReadIO()
        view.request = r
        qs = view.get_queryset()
        self.assertEqual(200, qs[0].value)


# ---------- MODELS ----------
class TestCompany(TestCase):
    def test_company_max_len(self):
        field = Company._meta.get_field('company').max_length
        self.assertEqual(50, field)


class TestCashTag(TestCase):
    def test_tag_max_len(self):
        field = CashTag._meta.get_field('tag').max_length
        self.assertEqual(50, field)


class TestCurrency(TestCase):
    def test_name_max_len(self):
        field = Currency._meta.get_field('name').max_length
        self.assertEqual(30, field)

    def test_symbol_max_len(self):
        field = Currency._meta.get_field('symbol').max_length
        self.assertEqual(3, field)

    def test_iso_code_max_len(self):
        field = Currency._meta.get_field('iso_code').max_length
        self.assertEqual(3, field)


class TestOneInOut(TestCase):
    def test_is_outcome(self):
        field = OneIO._meta.get_field('is_outcome').default
        self.assertTrue(field)

    def test_owner(self):
        field = OneIO._meta.get_field('owner')
        to_class = field.related_model
        field_on_delete = field.remote_field.on_delete
        self.assertTrue(issubclass(User, to_class))
        self.assertEqual(CASCADE, field_on_delete)

    def test_title(self):
        field = OneIO._meta.get_field('title').max_length
        self.assertEqual(50, field)

    def test_value(self):
        field_max = OneIO._meta.get_field('value').max_digits
        field_places = OneIO._meta.get_field('value').decimal_places
        self.assertEqual(17, field_max)
        self.assertEqual(2, field_places)

    def test_currency(self):
        field = OneIO._meta.get_field('currency')
        to_class = field.related_model
        field_on_delete = field.remote_field.on_delete
        self.assertTrue(issubclass(Currency, to_class))
        self.assertEqual(PROTECT, field_on_delete)

    def test_future(self):
        field = OneIO._meta.get_field('future').default
        self.assertTrue(field)

    def test_cash_tag(self):
        field = OneIO._meta.get_field('cash_tag')
        to_class = field.related_model
        field_on_delete = field.remote_field.on_delete
        field_null = field.null
        self.assertTrue(issubclass(CashTag, to_class))
        self.assertEqual(SET_NULL, field_on_delete)
        self.assertTrue(field_null)

    def test_company(self):
        field = OneIO._meta.get_field('company')
        to_class = field.related_model
        field_on_delete = field.remote_field.on_delete
        field_null = field.null
        self.assertTrue(issubclass(Company, to_class))
        self.assertEqual(SET_NULL, field_on_delete)
        self.assertTrue(field_null)

    def test_notes(self):
        field = OneIO._meta.get_field('notes').blank
        self.assertTrue(field)

    def test_creation_date(self):
        field = OneIO._meta.get_field('creation_date').auto_now_add
        self.assertTrue(field)

    def test_last_modification(self):
        field = OneIO._meta.get_field('last_modification').auto_now
        self.assertTrue(field)

    def test_ordering(self):
        o = User.objects.create()
        c = Currency.objects.create()

        vals = (100, 20, 30, 10)
        dates = ('1970-12-1', '1970-12-2', '1970-12-2', '1970-12-3')

        for v, d in zip(vals, dates):
            OneIO.objects.create(owner=o, value=v, currency=c, date=d)

        res = [obj.value for obj in OneIO.objects.all()]
        self.assertEqual([10, 30, 20, 100], res)

