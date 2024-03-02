# Creating sole propietorships 
class Company:
    def __init__(
            self, cash, account_receivables, inventory, current_assets #Current assets
            , noncurrent_assets , accu_depr, accu_depl #Other Assets
            , intangible_assets, longterm_investments #other assets
            , current_lia, noncurrent_lia # Liabilites
            , owners_equity, net_income , ebit  # Equity Accounts 
            , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement # Income statement Accounts
            ):
        
        # Assigning values to attributes
        self.cash = cash
        self.account_receivables = account_receivables
        self.inventory = inventory
        self.current_assets = current_assets
        
        # Non-current assets and deperciatables
        self.noncurrent_assets = noncurrent_assets
        self.accu_depr = accu_depr
        self.accu_depl = accu_depl
        self.intangible_assets = intangible_assets
        self.longterm_investments = longterm_investments
        
        # Liabilties
        self.current_lia = current_lia
        self.noncurrent_lia = noncurrent_lia
        
        # Equity
        self.owners_equity = owners_equity
        self.net_income = net_income 
        self.ebit = ebit        
        
        # Income Statements 
        self.total_rev = total_rev
        self.sales_rev = sales_rev
        self.total_exp = total_exp
        self.operating_exp = operating_exp
        self.interest_exp = interest_exp
        
    # Total assets calculation
    def total_assets(self):
        return self.cash + self.account_receivables + self.inventory +self.noncurrent_assets + self.current_assets + self.intangible_assets + self.longterm_investments - self.accu_depr - self.accu_depl
    
    # Total liabilities calculation
    def total_lia(self):  
        return self.current_lia + self.noncurrent_lia
    
#Hotel
class Hotel(Company):
    def __init__(
        self, room_num_aval, room_rev, room_num_occ, room_num_sold
        , cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        ):
        
       # initialize attributes from the base class within the subclasses super().__init__(
        super().__init__(
        cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        )
        
        self.room_num_aval = room_num_aval
        self.room_nun_occ = room_num_occ
        self.room_rev = room_rev
        self.room_num_sold = room_num_sold
        
#trade
class TradeSoleProp(Company):
    def __init__(
        self, cogs
        , cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        ):
        
       # initialize attributes from the base class within the subclasses super().__init__(
        super().__init__(
        cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        )
        
        self.cogs = cogs

#Agriculture
class Agriculture(Company):
    def __init__(
        self, total_farm_area, total_farm_rev, total_num_stock, total_stock_rev
        , cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit  # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        ):
        
       # initialize attributes from the base class within the subclasses super().__init__(
        super().__init__(
        cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        )
        
        self.total_farm_area = total_farm_area
        self.total_farm_rev = total_farm_rev
        self.total_num_stock = total_num_stock
        self.total_stock_rev = total_stock_rev
        
        
# Service businesses
class ServiceSector(Company):
    def __init__(
        self, client_num, total_fee_rev, equity_partner_num
        , cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        ):
        
       # initialize attributes from the base class within the subclasses super().__init__(
        super().__init__(
        cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        )
        
        self.client_num = client_num
        self.total_fee_rev = total_fee_rev
        self.equity_partner_num = equity_partner_num

# Manufacturing companies
class Manuf(Company):
    def __init__(
        self, materials_cost, overhead_cost, var_cost
        , cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        ):
        # initialize attributes from the base class within the subclasses
        super().__init__(
        cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , ebit # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        , sales_rev , total_exp, operating_exp, interest_exp  # Income Statement
        )
        self.materials_cost = materials_cost
        self.overhaed_cost = overhead_cost
        self.var_cost = var_cost
