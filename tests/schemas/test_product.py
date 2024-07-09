import pytest
from pydantic import ValidationError

from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_sucess():
    data = product_data()
    product = ProductIn(**data)
    # product = ProductIn.model_validate(data) (Mesma coisa que o de cima **data)

    assert product.name == "IPhone 14 pro Max"


def test_schemas_return_raise():
    with pytest.raises(ValidationError) as err:
        data = {"name": "IPhone 14 pro Max", "quantity": 10, "price": 8.500}
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "IPhone 14 pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.8/v/missing",
    }
