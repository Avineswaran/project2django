import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ecommerce.settings")
django.setup()

from faker import Faker

from supplier.models import Supplier
from Sparke.models import Customer
from dashboard.models import Invoice

def create_supplier(N):
    fake = Faker()
    for _ in range(N):
        Supplier.objects.create(
            supplierID          = fake.building_number(),
            supplierName        = fake.company(),
            brand               = fake.bs(),
            partCategory        = fake.bs(),
            vehicleType         = random.choice(['Car', 'Truck & Used Part']),
            billingMethod       = random.choice(['Ebill', 'Hardcopy', 'Hardcopy/Scanned']),
            longitude           = fake.longitude(),
            latitude            = fake.latitude(),
            transactionTerm     = random.choice(['30 Days Term', '60 Days Term','Cash Sale','TBA',]),
            streetAddr          = fake.street_address(),
            postalCode          = fake.postcode(),
            city                = fake.city(),
            state               = fake.street_suffix(),
            totalSupPts         = fake.building_number(),
        )

def create_order(N):
    fake = Faker()
    for _ in range(N):
        Invoice.objects.create(
            invoiceNo          = fake.building_number(),
            paymentID        = fake.building_number(),
            orderID        = fake.date_between(),
            invoiceDate            = fake.date_between(),
            custPhone         = fake.phone_number(),
            custAddr           = fake.street_address(),
            totalPayment        = fake.building_number(),
            quantity         = fake.building_number(),
        )

def create_dealer(N):
    fake = Faker()
    for _ in range(N):
        Customer.objects.create(
            user     = fake.first_name(),
            name        = fake.name(),
            phone       = fake.phone_number(),
            address  = fake.street_address(),
            postalCode  = fake.postcode(),
            city        = fake.city(),
            state       = fake.street_suffix(),
        )

create_supplier(70)
create_order(15)
create_dealer(34)

print("FAKED!")