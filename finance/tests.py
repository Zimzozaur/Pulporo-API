from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models import PROTECT, CASCADE, SET_NULL
from .models import Company, CashTag, Currency, OneInOut


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
        field = OneInOut._meta.get_field('is_outcome').default
        self.assertTrue(field)

    def test_owner(self):
        field = OneInOut._meta.get_field('owner')
        to_class = field.related_model
        field_on_delete = field.remote_field.on_delete
        self.assertTrue(issubclass(User, to_class))
        self.assertEqual(CASCADE, field_on_delete)

    def test_title(self):
        field = OneInOut._meta.get_field('title').max_length
        self.assertEqual(50, field)

    def test_value(self):
        field_max = OneInOut._meta.get_field('value').max_digits
        field_places = OneInOut._meta.get_field('value').decimal_places
        self.assertEqual(17, field_max)
        self.assertEqual(2, field_places)

    def test_currency(self):
        field = OneInOut._meta.get_field('currency')
        to_class = field.related_model
        field_on_delete = field.remote_field.on_delete
        self.assertTrue(issubclass(Currency, to_class))
        self.assertEqual(PROTECT, field_on_delete)

    def test_future(self):
        field = OneInOut._meta.get_field('future').default
        self.assertTrue(field)

    def test_cash_tag(self):
        field = OneInOut._meta.get_field('cash_tag')
        to_class = field.related_model
        field_on_delete = field.remote_field.on_delete
        field_null = field.null
        self.assertTrue(issubclass(CashTag, to_class))
        self.assertEqual(SET_NULL, field_on_delete)
        self.assertTrue(field_null)

    def test_company(self):
        field = OneInOut._meta.get_field('company')
        to_class = field.related_model
        field_on_delete = field.remote_field.on_delete
        field_null = field.null
        self.assertTrue(issubclass(Company, to_class))
        self.assertEqual(SET_NULL, field_on_delete)
        self.assertTrue(field_null)

    def test_notes(self):
        field = OneInOut._meta.get_field('notes').blank
        self.assertTrue(field)

    def test_creation_date(self):
        field = OneInOut._meta.get_field('creation_date').auto_now_add
        self.assertTrue(field)

    def test_last_modification(self):
        field = OneInOut._meta.get_field('last_modification').auto_now
        self.assertTrue(field)

    def test_ordering(self):
        o = User.objects.create()
        c = Currency.objects.create()

        vals = (100, 20, 30, 10)
        dates = ('1970-12-1', '1970-12-2', '1970-12-2', '1970-12-3')

        for v, d in zip(vals, dates):
            OneInOut.objects.create(owner=o, value=v, currency=c, date=d)

        res = [obj.value for obj in OneInOut.objects.all()]
        self.assertEqual([10, 30, 20, 100], res)

