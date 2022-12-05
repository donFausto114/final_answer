from django.http import JsonResponse
import json
from .models import Investments, Company
from django.db.models import Sum
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return JsonResponse({'text': 'Test'})

def add_company(request):

	if request.method == "POST":
		body = json.loads(request.body.decode('utf-8'))
		
		new_company = Company(company_name = body["company_name"], ticker=body["ticker"])
		new_company.save()
		
		return JsonResponse({'company_name': new_company.company_name, "ticker": new_company.ticker})


def test_buy_stocks(request):
	if request.method ==  "POST":
		body = json.loads(request.body.decode('utf-8'))
		company = Company.objects.get(ticker = body["ticker"])
		
		buying = Investments(investor=request.user, amount=body["amount"], company=company)
		buying.save()

		return JsonResponse({'company': str(buying.company.ticker), "user": str(buying.investor.username), "amount":buying.amount})


def get_portfolio(request):
	if request.method ==  "POST":
		body = json.loads(request.body.decode('utf-8'))
		user = User.objects.get(username=body["investor"])
		portfolio = Investments.objects.filter(investor = user).values('company__company_name').annotate(total_investments=Sum("amount"))
		fix_json = []

		for i in portfolio:
			fix_json.append(i)

		return JsonResponse({'portfolio': fix_json})

		


