# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in dollars.

| Parameter  | Values                    | Description                             |
|------------|---------------------------|-----------------------------------------|
| weight_kg  | positive float            | Shipment weight in kilograms            |
| zone       | `local`, `regional`       | Delivery zone                           |
| service    | `standard`, `express`     | Service level (default: `standard`)     |

Express shipping adds **$7.00** to the standard rate. Unknown zones or services
raise `ValueError`.

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```
# Standard quote: 2 kg, local zone
python -m warehouse.cli 2 local
# → $8.00

# Express quote: 2 kg, regional zone
python -m warehouse.cli 2 regional --service express
# → $18.00
```
