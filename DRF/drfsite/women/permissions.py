from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):  # Ограничение прав доступа на уровне всего запроса
        # проверка на безопасный запрос (запрос на чтение, а не изменение)
        if request.method in permissions.SAFE_METHODS:
            return True  # если возвращаем "True", то права доступа предоставлены, если "False", то нет

        # следующая строка делает проверку на то, что в систему зашел АДМИН
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    # Используем метод "has_object_permission", т.к. мы тут уже работаем с записями
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # проверка на безопасность
            return True

        return obj.user == request.user  # если пользователь из БД = пользователю по запросу, то даем доступ
