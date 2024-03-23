from django.urls import path

from basic_app import views


app_name = "basic_app"   

urlpatterns = [
    path("", views.HomePage.as_view(), name='home'),
    path("register/", views.SignUpView.as_view(), name="signup"),
    path("confirm-payment/", views.upload_receipt, name="receipt"),
    path('dashboard-home/', views.user_dashboard_view, name='user_dashboard'),
    path('dashboard-profit/', views.user_profit_record_view, name='user_profit-record'),
    path('dashboard-transaction/', views.user_transaction_record_view, name='user_transaction-record'),
    path("confirmation-complete/", views.DashBoardVerify.as_view(), name="verify"),
    path("kyc/", views.upload_kyc, name="kyc"),
    path("kyc-verify/", views.DashBoardKYCVerify.as_view(), name="verify-kyc"),
    path("login/", views.login_request, name="login"),
    path('logout/', views.logout_request, name='logout'),
    path("refer/", views.Refer.as_view(), name="refer"),
    path("why_us/", views.WhyUs.as_view(), name="why_us"),
    path("contact_us/", views.ContactUs.as_view(), name="contact_us"),
    path("company_news/", views.CompanyNews.as_view(), name="company_news"),
    path("global_awards/", views.GlobalAwards.as_view(), name="global_awards"),
    path("privacy_policy/", views.PrivacyPolicy.as_view(), name="privacy"),
    path("risk_warning/", views.RiskWarning.as_view(), name="risk_warning"),
    path("safety_funds/", views.SafetyFunds.as_view(), name="safety_funds"),
    path("license/", views.License.as_view(), name="license"),
    path("terms_condtions/", views.Terms.as_view(), name="terms"),
    path("faq/", views.FAQ.as_view(), name="faq"),
    path("products_forex/", views.ProductForex.as_view(), name="products_forex"),
    path("products_CFDs/", views.CFDs.as_view(), name="products_cfds"),
    path("products_stock/", views.Stock.as_view(), name="products_stock"),
    path("products_crypto/", views.Crypto.as_view(), name="products_crypto"),
    path("products_metal", views.Metal.as_view(), name="products_metal"),
    path("products_futures/", views.Futures.as_view(), name="products_futures"),
    path("products_shares/", views.Shares.as_view(), name="products_shares"),
    path("products_indices/", views.Indices.as_view(), name="products_indices"),
    path("products_energies/", views.Energies.as_view(), name="products_energies"),
    path("products_bonds/", views.Bonds.as_view(), name="products_bonds"),
    path("products_commodities/", views.Commodity.as_view(), name="products_commodities"),
    path("education_forex/", views.Forex.as_view(), name="education_forex"),
    path("education_cfd-advantage/", views.CFDAdvantage.as_view(), name="education_cfd-advantage"),
    path("education_fx-strategy/", views.FxStrategy.as_view(), name="education_fx-strategy"),
    path("education_cfd-trading/", views.CFDTrading.as_view(), name="education_cfd-trading"),
    path("education_cfd-risk/", views.CFDRisk.as_view(), name="education_cfd-risk"),
    path("education_cfd-glossary/", views.CFDGlossary.as_view(), name="education_cfd-glossary"),
    path("accounts_types/", views.AccountTypes.as_view(), name="accounts_types"),
    path("accounts_spreads/", views.Spreads.as_view(), name="accounts_spreads"),
    path("accounts_deposit-withdrawal/", views.DepositWithdrawal.as_view(), name="accounts_deposit-withdraw"),
    path("accounts_trading-conditions/", views.TradingConditions.as_view(), name="accounts_trading-conditions"),
    path("accounts_trading-platforms/", views.TradingPlatforms.as_view(), name="accounts_trading-platforms"),
    path("dashboard-home/", views.DashboardLight.as_view(), name="dashboard-light"),
    path("dashboard-support/", views.DashboardHelpLight.as_view(), name="dashboard-help"),
    path("dashboard-invest/", views.DashboardInvestLight.as_view(), name="dashboard-invest"),
    path("dashboard-referral/", views.DashBoardReferral.as_view(), name="dashboard-referral"),
    path("dashboard-profit/", views.DashboardProfitLight.as_view(), name="dashboard-profit"),
    path("dashboard-transaction/", views.DashboardTransactionLight.as_view(), name="dashboard-transaction"),
    path("dashboard-payment/", views.DashBoardPayment.as_view(), name="payment"),
    path("dashboard-payment-usdt/", views.DashBoardUsdt.as_view(), name="usdt"),
    path("dashboard-payment-ethereum/", views.DashBoardEthereum.as_view(), name="ethereum"),
    path("dashboard-payment-bitcoin/", views.DashBoardBitcoin.as_view(), name="bitcoin"),
    path("dashboard-withdraw/", views.DashBoardWithdrawal.as_view(), name="withdrawal"),
    path("dashboard-withdraw-usdt/", views.DashBoardWithdrawalUSDT.as_view(), name="withdrawal-usdt"),
    path("dashboard-withdraw-ethereum/", views.DashBoardWithdrawalEthereum.as_view(), name="withdrawal-ethereum"),
    path("dashboard-withdraw-bitcoin/", views.DashBoardWithdrawalBitcoin.as_view(), name="withdrawal-bitcoin"),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
