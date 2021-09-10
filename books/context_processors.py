from books.forms import UploadBookForm


def get_books(request):
    if request.user.is_authenticated:
        return {
            'books': request.user.books.all()
        }
    return []

def get_upload_form(request):
    form = UploadBookForm()
    return {
        'form': form
    }
