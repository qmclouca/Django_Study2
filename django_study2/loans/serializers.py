from rest_framework import serializers
from .models import Loan
from books.serializers import BookSerializer

class LoanSerializer(serializers.ModelSerializer):
    book = BookSerializer()  # Serializer aninhado para exibir os detalhes do livro

    class Meta:
        model = Loan
        fields = ['id', 'book', 'borrower', 'loan_date', 'return_date']
