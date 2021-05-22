def upload_book_to(instance, filename):
    return f'{instance.owner.username}/{filename}'
