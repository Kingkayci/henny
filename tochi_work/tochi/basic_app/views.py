from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .forms import ImageUploadForm, KYCUploadForm
from .models import AccountBalance
from django.contrib.auth.decorators import login_required

@login_required
def user_dashboard_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user
    
    # Pass the account_balance instance to the template
    return render(request, template_name='dashboard/dashboard-l.html', context={'account_balance':account_balance})


@login_required
def user_profit_record_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user
    
    # Pass the account_balance instance to the template
    return render(request, template_name='dashboard/profit-l.html', context={'account_balance':account_balance})



@login_required
def user_transaction_record_view(request):
    # Retrieve the AccountBalance instance for the logged-in user
    try:
        account_balance = AccountBalance.objects.get(user=request.user)
    except AccountBalance.DoesNotExist:
        account_balance = None  # Handle the case where AccountBalance does not exist for the user
    
    # Pass the account_balance instance to the template
    return render(request, template_name='dashboard/transaction-l.html', context={'account_balance':account_balance})



def upload_receipt(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basic_app:verify')
    else:
        form = ImageUploadForm()
    return render(request, template_name='dashboard/receipt.html', context={'receipt_form':form})


def upload_kyc(request):
    if request.method == "POST":
        form = KYCUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basic_app:verify-kyc')
    else:
        form = KYCUploadForm()
    return render(request, template_name='dashboard/kyc.html', context={'kyc_form':form})    


class HomePage(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy('basic_app:login')
    template_name = 'form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password= password)

            if user is not None:
                login(request, user)
                return redirect('basic_app:dashboard-light')
        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request, template_name='login.html', context={'login':form})

def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('basic_app:login')


class Refer(TemplateView):
    template_name = 'refer.html'

class WhyUs(TemplateView):
    template_name = 'about_us/why_us.html'

class ContactUs(TemplateView):
    template_name = 'about_us/contact_us.html'

class CompanyNews(TemplateView):
    template_name = 'about_us/company_news.html'

class GlobalAwards(TemplateView):
    template_name = 'about_us/global_awards.html'

class PrivacyPolicy(TemplateView):
    template_name = 'about_us/privacy_policy.html'

class RiskWarning(TemplateView):
    template_name = 'about_us/risk_warning.html'

class SafetyFunds(TemplateView):
    template_name = 'about_us/safety_funds.html'

class License(TemplateView):
    template_name = 'about_us/licenses.html'

class Terms(TemplateView):
    template_name = 'about_us/terms_conditions.html'

class FAQ(TemplateView):
    template_name = 'about_us/faq.html'



class ProductForex(TemplateView):
    template_name = 'products/forex.html'

class CFDs(TemplateView):
    template_name = 'products/cfd.html'

class Stock(TemplateView):
    template_name = 'products/stock.html'

class Crypto(TemplateView):
    template_name = 'products/crypto.html'

class Metal(TemplateView):
    template_name = 'products/metals.html'

class Futures(TemplateView):
    template_name = 'products/futures.html'

class Shares(TemplateView):
    template_name = 'products/shares.html'

class Indices(TemplateView):
    template_name = 'products/indices.html'
    
class Energies(TemplateView):
    template_name = 'products/energies.html'

class Bonds(TemplateView):
    template_name = 'products/bonds.html'

class Commodity(TemplateView):
    template_name = 'products/commodities.html'


class Forex(TemplateView):
    template_name = 'education/forex.html'

class CFDAdvantage(TemplateView):
    template_name = 'education/cfd_advantage.html'

class FxStrategy(TemplateView):
    template_name = 'education/fx_strategies.html'

class CFDTrading(TemplateView):
    template_name = 'education/cfd_trading.html'

class CFDRisk(TemplateView):
    template_name = 'education/cfd_risk.html'

class CFDGlossary(TemplateView):
    template_name = 'education/cfd_glossary.html'


class AccountTypes(TemplateView):
    template_name = 'accounts/account_types.html'

class Spreads(TemplateView):
    template_name = 'accounts/spreads.html'

class DepositWithdrawal(TemplateView):
    template_name = 'accounts/deposit_withdrawal.html'

class TradingConditions(TemplateView):
    template_name = 'accounts/trading_conditions.html'

class TradingPlatforms(TemplateView):
    template_name = 'accounts/trading_platforms.html'


class DashboardLight(TemplateView):
    template_name = 'dashboard/dashboard-l.html'

class DashboardHelpLight(TemplateView):
    template_name = 'dashboard/help_support-l.html'

class DashboardInvestLight(TemplateView):
    template_name = 'dashboard/invest-l.html'

class DashboardKYC(TemplateView):
    template_name = 'dashboard/kyc.html'

class DashboardProfitLight(TemplateView):
    template_name = 'dashboard/profit-l.html'

class DashboardTransactionLight(TemplateView):
    template_name = 'dashboard/transaction-l.html'

class DashBoardReferral(TemplateView):
    template_name = 'dashboard/referral.html'

class DashBoardPayment(TemplateView):
    template_name = 'dashboard/payment.html'

class DashBoardUsdt(TemplateView):
    template_name = 'dashboard/usdt.html'

class DashBoardEthereum(TemplateView):
    template_name = 'dashboard/ethereum.html'

class DashBoardBitcoin(TemplateView):
    template_name = 'dashboard/bitcoin.html'

class DashBoardWithdrawal(TemplateView):
    template_name = 'dashboard/withdrawal.html'

class DashBoardWithdrawalUSDT(TemplateView):
    template_name = 'dashboard/withdrawal-usdt.html'

class DashBoardWithdrawalEthereum(TemplateView):
    template_name = 'dashboard/withdrawal-ethereum.html'

class DashBoardWithdrawalBitcoin(TemplateView):
    template_name = 'dashboard/withdrawal-bitcoin.html'

class DashBoardVerify(TemplateView):
    template_name = 'dashboard/verify.html'

class DashBoardKYCVerify(TemplateView):
    template_name = 'dashboard/verifykyc.html'
    