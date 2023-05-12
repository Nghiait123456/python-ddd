import enum


class OrderState(enum.Enum):
    PAYMENT_WAITING = 'PAYMENT_WAITING'
    PREPARING = 'PREPARING'
    SHIPPED = 'SHIPPED'
    DELIVERING = 'DELIVERING'
    DELIVERY_COMPLETED = 'DELIVERY_COMPLETED'
    CANCELED = 'CANCELED'