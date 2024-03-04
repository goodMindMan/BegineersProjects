# Creating main class
class Company:
    def __init__(
            self, cash, account_receivables, inventory, current_assets 
            , noncurrent_assets , accu_depr 
            , intangible_assets, longterm_investments 
            , current_lia, noncurrent_lia 
            , owners_equity, net_income , ebit   
            , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp
            ):
        
        # Assigning values to attributes
        # Current Assets
        self.cash = cash
        self.account_receivables = account_receivables
        self.inventory = inventory
        self.current_assets = current_assets
        
        # Non-current assets and deperciatables
        self.noncurrent_assets = noncurrent_assets
        self.accu_depr = accu_depr
        self.intangible_assets = intangible_assets
        self.longterm_investments = longterm_investments
        
        # Liabilties
        self.current_lia = current_lia
        self.noncurrent_lia = noncurrent_lia
        
        # Equity
        self.owners_equity = owners_equity
        self.net_income = net_income 
        self.ebit = ebit        
        
        # Income s 
        self.total_rev = total_rev
        self.sales_rev = sales_rev
        self.total_exp = total_exp
        self.operating_exp = operating_exp
        self.interest_exp,  = interest_exp
        self.depr_exp = depr_exp
        self.wages_exp = wages_exp
    
    # Totals Methods
    # - Total assets calculation
    def total_assets(self):
        return self.cash + self.account_receivables + self.inventory +self.noncurrent_assets + self.current_assets + self.intangible_assets + self.longterm_investments - self.accu_depr
    
    # - Total liabilities calculation
    def total_lia(self):  
        return self.current_lia + self.noncurrent_lia

    # Financial Ratios methods
    # - Liquidity ratio calculation
    # -- Current Ratio
    def current_ratio(self):
        return self.current_assets / self.current_lia
    
    # -- Quick ratio
    def quick_ratio(self):
        return (self.current_assets - self.inventory) / self.current_lia
    
    # --Cash ratio
    def cash_ratio(self):
        return self.cash / self.current_lia
    
    # - Financial leverage
    # -- Total dept ratio
    def total_debt_ratio(self):
        return (self.total_assets() - self.owners_equity) / self.total_assets() 
    
    # -- Dept Equity ratio
    def dept_equity_ratio(self):
        return self.total_lia() / self.owners_equity
    
    # -- Equity Multiplier
    def equity_multi(self):
        return self.total_assets() / self.owners_equity
    
    # -- Times interest earned ratio
    def tie(self):
        return self.ebit / self.interest_exp
    
    # -- Cash Coverage Ratios
    def cash_cov_ratio(self):
        return (self.ebit + self.depr_exp) / self.interest_exp
    
    # - Turnover Measures
    # -- Receivables turnover
    def rece_trnovr(self):
        return self.sales_rev / self.account_receivables
    
    # -- Days’ sales in receivables
    def days_sales_rece_trnover(self):
        return 365 / self.rece_trnovr()
    
    #  -- Total asset turnover
    def total_asset_trnovr(self):
        return self.sales_rev / self.total_assets()
    
    # - Profitability Measures
    # -- Profit margin
    def profit_marg(self):
        return self.net_income / self.total_rev
    
    # -- Return on assets
    def return_assets(self):
        return self.net_income / self.total_assets()
    
    # -- Return on equity
    def return_assets(self):
        return self.net_income / self.owners_equity
    
    def wages_rev_ratio(self):
        return self.wages_exp / self.total_rev
    
#Hotel
class Hotel(Company):
    def __init__(
        self, room_num_aval, room_rev, room_num_occ, room_num_sold
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        ):
        
       # initialize attributes from the base class within the subclasses
        super().__init__(
        cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
        
        # Intializing subclass attributes
        self.room_num_aval = room_num_aval
        self.room_num_occ = room_num_occ
        self.room_rev = room_rev
        self.room_num_sold = room_num_sold
    
    # Other metrics methods
    # gross operation profit calculation 
    def GOP(self):
        return self.total_rev - self.operating_exp
    
    # Occupation rate
    def occ_rate(self):
        return self.room_num_occ / self.room_num_aval
    
    # Specific Financial Ratios methods
    # Average daily rate
    def ave_daily_rate(self):
        return self.room_rev / self.room_num_occ
    
    # Revenue per available rooms
    def rev_per_room_aval(self):
        return self.room_rev / self.room_num_aval
    
    # Gross Operating Profit per Available Room
    def GOPPAR(self):
        return self.GOP() / self.room_num_aval
    
    # Revenue Per Available Rooms
    def rev_par(self):
        return self.ave_daily_rate() * self.occ_rate()
    

        
#trade
class TradeSoleProp(Company):
    def __init__(
        self, cogs
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        ):
        
        # initialize attributes from the base class within the subclasses
        super().__init__(
        cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
        
        # Intializing subclass attributes
        self.cogs = cogs

    # Specific Financial Ratios methods
    # Inventory turnover 
    def inv_trnovr(self):
        return self.cogs / self.inventory
    
        # Days’ sales in inventory 
    def days_sales_inv_trnovr(self):
        return 365 / self.days_sales_inv_trnovr
        

#Agriculture
class Agriculture(Company):
    def __init__(
        self, total_farm_area, total_farm_rev, total_num_stock, total_stock_rev
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit   
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        ):
        
        # initialize attributes from the base class within the subclasses
        super().__init__(
        cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
        
        # Intializing subclass attributes
        self.total_farm_area = total_farm_area
        self.total_farm_rev = total_farm_rev
        self.total_num_stock = total_num_stock
        self.total_stock_rev = total_stock_rev

    # Specific Financial Ratios methods
    # yield per unit of area
    def land_yield(self):
        return self.total_farm_rev / self.total_farm_area
    
    # yield per livestock
    def livestock_yield(self):
        return self.total_stock_rev / self.total_num_stock


# Service businesses
class ServiceSector(Company):
    def __init__(
        self, total_fee_rev, equity_partner_num, consultant_num
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        ):
        
        # initialize attributes from the base class within the subclasses
        super().__init__(
        cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
        
        # Intializing subclass attributes
        self.total_fee_rev = total_fee_rev
        self.equity_partner_num = equity_partner_num
        self.consultant_num = consultant_num
    
    # Specific Financial Ratios methods
    # profit margin per partner
    def profit_marg_partner(self):
        return self.net_income / self.equity_partner_num
    
    # fees revenue per consultant or lawyer
    def fee_rev_consultant_ratio(self):
        return self.total_fee_rev / self.consultant_num


# Manufacturing companies
class Manuf(Company):
    def __init__(
        self, mtrils_cost, cogs, manuf_cost
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        ):

        # initialize attributes from the base class within the subclasses
        super().__init__(
        cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        , sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
        
        # Initializing subclass attributes
        self.mtrils_cost = mtrils_cost
        self.cogs = cogs
        self.manuf_cost = manuf_cost
    
    # Specific Financial Ratios methods
    # Inventory turnover
    def inv_trnovr(self):
        return self.cogs / self.inventory
    
    # Manufacturing costs to expenses ratio
    def manuf_cost_exp_ratio(self):
        return self.manuf_cost / self.total_exp
    
    # Materials costs to expenses ratio
    def mtrils_cost_exp_ratio(self):
        return self.mtrils_cost / self.total_exp
    

# Mining and forestry
class mining_forestry(Company):
    def __init__(
        self, accu_depl, depl_exp
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        ):
        
        # initialize attributes from the base class within the subclasses
        super().__init__(
        cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        , sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
        
        # Initializing subclass attributes
        self.accu_depl = accu_depl
        self.depl_exp = depl_exp
        
    # Total assets after accumulated depletion
    def total_assets(self):
        return self.cash + self.account_receivables + self.inventory +self.noncurrent_assets + self.current_assets + self.intangible_assets + self.longterm_investments - self.accu_depr - self.accu_depl
    
    # Ignored inherited methods that included `total_assets()` due to change in the calculation of assets (subtracting accumulated depletion)
    # ignored inherited method `cash_cov_ratio` due to adding depl exp
    # -- Total dept ratio
    def total_debt_ratio(self):
        return (self.total_assets() - self.owners_equity) / self.total_assets()
    
    # -- Equity Multiplier
    def equity_multi(self):
        return self.total_assets() / self.owners_equity
    
    #  -- Total asset turnover
    def total_asset_trnovr(self):
        return self.sales_rev / self.total_assets()
    
    # -- Return on assets
    def return_assets(self):
        return self.net_income / self.total_assets()
    
    # -- Cash Coverage Ratios
    def cash_cov_ratio(self):
        return (self.ebit + self.depr_exp + self.depl_exp) / self.interest_exp
