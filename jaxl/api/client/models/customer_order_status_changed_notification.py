"""
Copyright (c) 2010-present by Jaxl Innovations Private Limited.

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, is strictly prohibited.
"""

import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.customer_order_status_changed_notification_type_enum import (
    CustomerOrderStatusChangedNotificationTypeEnum,
)
from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.customer_order_status_changed_notification_attributes import (
        CustomerOrderStatusChangedNotificationAttributes,
    )
    from ..models.customer_order_status_changed_notification_order_attributes import (
        CustomerOrderStatusChangedNotificationOrderAttributes,
    )


T = TypeVar("T", bound="CustomerOrderStatusChangedNotification")


@attr.s(auto_attribs=True)
class CustomerOrderStatusChangedNotification:
    """
    Attributes:
        dispatched_at (datetime.datetime): Datetime when this notification was dispatched
        type (CustomerOrderStatusChangedNotificationTypeEnum):
        app_user_id (int): AppUser who made this purchase.
        order_id (int): Customer order ID from the payments backend.
        original_order_id (int): Order ID from the payments backend.
        item (str): Purchased item
        parent_order_id (Union[Unset, None, int]): Populated for resubscribed events to indicate parent order id
        sku (Union[Unset, None, str]): Optionally, a product SKU associated with this order.
        upcoming_invoice_timestamp (Union[Unset, None, datetime.datetime]): Only available for 'will_review'
            notification type
        paid_till (Union[Unset, None, datetime.datetime]): Only available for subscriptions when notification types are
            `purchased`, `renewed`, `resubscribed`. This is typically equal to now + plan duration in days.
        paid_for (Union[Unset, None, int]): Only available for subscriptions  when notification types are `purchased`,
            `renewed`, `resubscribed`.This is typically equal to plan duration in seconds.
        attributes (Union[Unset, None, CustomerOrderStatusChangedNotificationAttributes]): Contains attributes of an
            AppItem (i.e.country_id, number_type)
        order_attributes (Union[Unset, None, CustomerOrderStatusChangedNotificationOrderAttributes]): Order's metadata
    """

    dispatched_at: datetime.datetime
    type: CustomerOrderStatusChangedNotificationTypeEnum
    app_user_id: int
    order_id: int
    original_order_id: int
    item: str
    parent_order_id: Union[Unset, None, int] = UNSET
    sku: Union[Unset, None, str] = UNSET
    upcoming_invoice_timestamp: Union[Unset, None, datetime.datetime] = UNSET
    paid_till: Union[Unset, None, datetime.datetime] = UNSET
    paid_for: Union[Unset, None, int] = UNSET
    attributes: Union[
        Unset, None, "CustomerOrderStatusChangedNotificationAttributes"
    ] = UNSET
    order_attributes: Union[
        Unset, None, "CustomerOrderStatusChangedNotificationOrderAttributes"
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dispatched_at = self.dispatched_at.isoformat()

        type = self.type.value

        app_user_id = self.app_user_id
        order_id = self.order_id
        original_order_id = self.original_order_id
        item = self.item
        parent_order_id = self.parent_order_id
        sku = self.sku
        upcoming_invoice_timestamp: Union[Unset, None, str] = UNSET
        if not isinstance(self.upcoming_invoice_timestamp, Unset):
            upcoming_invoice_timestamp = (
                self.upcoming_invoice_timestamp.isoformat()
                if self.upcoming_invoice_timestamp
                else None
            )

        paid_till: Union[Unset, None, str] = UNSET
        if not isinstance(self.paid_till, Unset):
            paid_till = self.paid_till.isoformat() if self.paid_till else None

        paid_for = self.paid_for
        attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict() if self.attributes else None

        order_attributes: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.order_attributes, Unset):
            order_attributes = (
                self.order_attributes.to_dict() if self.order_attributes else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dispatched_at": dispatched_at,
                "type": type,
                "app_user_id": app_user_id,
                "order_id": order_id,
                "original_order_id": original_order_id,
                "item": item,
            }
        )
        if parent_order_id is not UNSET:
            field_dict["parent_order_id"] = parent_order_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if upcoming_invoice_timestamp is not UNSET:
            field_dict["upcoming_invoice_timestamp"] = upcoming_invoice_timestamp
        if paid_till is not UNSET:
            field_dict["paid_till"] = paid_till
        if paid_for is not UNSET:
            field_dict["paid_for"] = paid_for
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if order_attributes is not UNSET:
            field_dict["order_attributes"] = order_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_order_status_changed_notification_attributes import (
            CustomerOrderStatusChangedNotificationAttributes,
        )
        from ..models.customer_order_status_changed_notification_order_attributes import (
            CustomerOrderStatusChangedNotificationOrderAttributes,
        )

        d = src_dict.copy()
        dispatched_at = isoparse(d.pop("dispatched_at"))

        type = CustomerOrderStatusChangedNotificationTypeEnum(d.pop("type"))

        app_user_id = d.pop("app_user_id")

        order_id = d.pop("order_id")

        original_order_id = d.pop("original_order_id")

        item = d.pop("item")

        parent_order_id = d.pop("parent_order_id", UNSET)

        sku = d.pop("sku", UNSET)

        _upcoming_invoice_timestamp = d.pop("upcoming_invoice_timestamp", UNSET)
        upcoming_invoice_timestamp: Union[Unset, None, datetime.datetime]
        if _upcoming_invoice_timestamp is None:
            upcoming_invoice_timestamp = None
        elif isinstance(_upcoming_invoice_timestamp, Unset):
            upcoming_invoice_timestamp = UNSET
        else:
            upcoming_invoice_timestamp = isoparse(_upcoming_invoice_timestamp)

        _paid_till = d.pop("paid_till", UNSET)
        paid_till: Union[Unset, None, datetime.datetime]
        if _paid_till is None:
            paid_till = None
        elif isinstance(_paid_till, Unset):
            paid_till = UNSET
        else:
            paid_till = isoparse(_paid_till)

        paid_for = d.pop("paid_for", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, None, CustomerOrderStatusChangedNotificationAttributes]
        if _attributes is None:
            attributes = None
        elif isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CustomerOrderStatusChangedNotificationAttributes.from_dict(
                _attributes
            )

        _order_attributes = d.pop("order_attributes", UNSET)
        order_attributes: Union[
            Unset, None, CustomerOrderStatusChangedNotificationOrderAttributes
        ]
        if _order_attributes is None:
            order_attributes = None
        elif isinstance(_order_attributes, Unset):
            order_attributes = UNSET
        else:
            order_attributes = (
                CustomerOrderStatusChangedNotificationOrderAttributes.from_dict(
                    _order_attributes
                )
            )

        customer_order_status_changed_notification = cls(
            dispatched_at=dispatched_at,
            type=type,
            app_user_id=app_user_id,
            order_id=order_id,
            original_order_id=original_order_id,
            item=item,
            parent_order_id=parent_order_id,
            sku=sku,
            upcoming_invoice_timestamp=upcoming_invoice_timestamp,
            paid_till=paid_till,
            paid_for=paid_for,
            attributes=attributes,
            order_attributes=order_attributes,
        )

        customer_order_status_changed_notification.additional_properties = d
        return customer_order_status_changed_notification

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
