"""Модуль содержит функции, которые обрабатывают HTTP исключения."""

from fastapi import HTTPException, status


def not_found(entity: str) -> HTTPException:
    """
    Возвращает исключение 404 Not Found.

    :param entity: Название сущности, которая не найдена (например, "User").
    :type entity: str
    :return: HTTPException с кодом 404 и сообщением о не найденной сущности.
    :rtype: HTTPException
    """

    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{entity} not found"
    )

def bad_request(detail: str = "Bad request") -> HTTPException:
    """
    Возвращает исключение 400 Bad Request.

    :param detail: Описание ошибки (по умолчанию: "Bad request").
    :type detail: str
    :return: HTTPException с кодом 400 и сообщением об ошибке.
    :rtype: HTTPException
    """

    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail
    )