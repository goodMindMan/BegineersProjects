# Creating sole propietorships 
class SolePropietorship:
    def __init__(
            self, cash, account_receivables, inventory, current_assets #Current assets
            , noncurrent_assets , accu_depr, accu_depl #Other Assets
            , intangible_assets, longterm_investments #other assets
            , current_lia, noncurrent_lia # Liabilites
            , owners_equity, net_income , __edit__ # Equity Accounts 
            , total_rev, sales_rev , total_exp, operating_exp, interest_exp # Income statement Accounts
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
        self.__edit__ = __edit__       
        
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
class Hotel(SolePropietorship):
    def __init__(
        self, room_num_aval, room_rev, room_num_occ, room_num_sold
        , cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , __edit__# Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp
        ):
        super().__init__(
            cash, account_receivables, inventory, current_assets #Current assets
            , noncurrent_assets , accu_depr, accu_depl #Other Assets
            , intangible_assets, longterm_investments #other assets
            , current_lia, noncurrent_lia # Liabilites
            , owners_equity, net_income , __edit__# Equity Accounts 
            , total_rev, sales_rev , total_exp, operating_exp, interest_exp
        )
        self.room_num_aval = room_num_aval
        self.room_nun_occ = room_num_occ
        self.room_rev = room_rev
        self.room_num_sold = room_num_sold
        
#trade
class TradeSoleProp(SolePropietorship):
    def __init__(
        self, cogs
        , cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , __edit__# Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp
        ):
        super().__init__(
        cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , __edit__# Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp
        )
        self.cogs = cogs

#Agriculture
class Agriculture(SolePropietorship):
    def __init__(
        self, total_farm_area, total_farm_rev, total_num_stock, total_stock_rev
        , cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , __edit__ # Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp
        ):
        super().__init__(
        cash, account_receivables, inventory, current_assets #Current assets
        , noncurrent_assets , accu_depr, accu_depl #Other Assets
        , intangible_assets, longterm_investments #other assets
        , current_lia, noncurrent_lia # Liabilites
        , owners_equity, net_income , __edit__# Equity Accounts 
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp
        )
        self.total_farm_area = total_farm_area
        self.total_farm_rev = total_farm_rev
        self.total_num_stock = total_num_stock
        self.total_stock_rev = total_stock_rev
        
        
#consulting
class Consulting(SolePropietorship):
    def __init__(self):
        pass