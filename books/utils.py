def upload_book_to(instance, filename):
    return f'{instance.owner.email.split("@")[0]}/{filename}'
