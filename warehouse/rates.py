"""Shipping rate calculations."""


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Weight in kilograms (must be positive).
        zone: Delivery zone ('local' or 'regional').
        service: Shipping service level ('standard' or 'express').
                 Express adds $7.00 to the standard rate.

    Returns:
        Shipping cost in dollars, rounded to two decimal places.

    Raises:
        ValueError: If weight_kg is not positive, zone is unknown,
                    or service is unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in {"standard", "express"}:
        raise ValueError("unknown service")
    base = 5.0 if zone == "local" else 8.0
    cost = base + 1.5 * weight_kg
    if service == "express":
        cost += 7.0
    return round(cost, 2)
