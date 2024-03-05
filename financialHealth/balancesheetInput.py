import classCreation as clss
# Functions to input company information
# Intializing some variables
prmpt1 = 'Please enter a number'
prmpt2 = 'Enter values in order: --> '
# Hotels
def create_hotel(comp_name):
    print('Please enter in that order:\nHotel Specific metrics:\n----------------\nroom_num_aval\nroom_rev\nroom_num_occ\nroom_num_sold\n----------------\nRequired balance Sheet info:\ncash\naccount_receivables\ninventory\ncurrent_assets\nnoncurrent_assets\naccu_depr\nintangible_assets\nlongterm_investments\ncurrent_lia\nnoncurrent_lia\nowners_equity\nnet_income\nebit\ntotal_rev\nsales_rev\ntotal_exp\noperating_exp\ninterest_exp\ndepr_exp\nwages_exp')
    inc_hotel_loop = 0    
    blnc_sht_lst = []
    while inc_hotel_loop < 24:
        try:
            in_amount = float(input(prmpt2))
            blnc_sht_lst.append(in_amount) 
            inc_hotel_loop += 1
        except ValueError:
            print(prmpt1)
    comp_name = clss.Hotel(*blnc_sht_lst)

# Trading
def create_trading_co(comp_name):
    print('Please enter in that order:\ntrading Specific metrics:\n----------------\ncogs\n----------------\nRequired balance Sheet info:\ncash\naccount_receivables\ninventory\ncurrent_assets\nnoncurrent_assets\naccu_depr\nintangible_assets\nlongterm_investments\ncurrent_lia\nnoncurrent_lia\nowners_equity\nnet_income\nebit\ntotal_rev\nsales_rev\ntotal_exp\noperating_exp\ninterest_exp\ndepr_exp\nwages_exp')
    inc_trade_loop = 0
    blnc_sht_lst = []
    while inc_trade_loop < 21:
        try:
            in_amount = float(input(prmpt2))
            blnc_sht_lst.append(in_amount) 
            inc_trade_loop += 1
        except ValueError:
            print(prmpt1)
    comp_name = clss.Trade(*blnc_sht_lst)

# Agriculture and farms
def create_farm(comp_name):
    print('Please enter in that order:\nAgriculture Specific metrics:\n----------------\ntotal_farm_area\ntotal_farm_rev\ntotal_num_stock\ntotal_stock_rev\n----------------\nRequired balance Sheet info:\ncash\naccount_receivables\ninventory\ncurrent_assets\nnoncurrent_assets\naccu_depr\nintangible_assets\nlongterm_investments\ncurrent_lia\nnoncurrent_lia\nowners_equity\nnet_income\nebit\ntotal_rev\nsales_rev\ntotal_exp\noperating_exp\ninterest_exp\ndepr_exp\nwages_exp')
    inc_agri_loop = 0
    blnc_sht_lst = []
    while inc_agri_loop < 24:
        try:
            in_amount = float(input(prmpt2))
            blnc_sht_lst.append(in_amount) 
            inc_agri_loop += 1
        except ValueError:
            print(prmpt1)
    comp_name = clss.Agriculture(*blnc_sht_lst)

# Professional Services
def create_srvcs_co(comp_name):
    print('Please enter in that order:\nServicesSector Specific metrics:\n----------------\ntotal_fee_rev\nequity_partner_num\nconsultant_num\n----------------\nRequired balance Sheet info:\ncash\naccount_receivables\ninventory\ncurrent_assets\nnoncurrent_assets\naccu_depr\nintangible_assets\nlongterm_investments\ncurrent_lia\nnoncurrent_lia\nowners_equity\nnet_income\nebit\ntotal_rev\nsales_rev\ntotal_exp\noperating_exp\ninterest_exp\ndepr_exp\nwages_exp')
    inc_srvcs_loop = 0
    blnc_sht_lst = []
    while inc_srvcs_loop < 23:
        try:
            in_amount = float(input(prmpt2))
            blnc_sht_lst.append(in_amount) 
            inc_srvcs_loop += 1
        except ValueError:
            print(prmpt1)
    comp_name = clss.ServiceSector(*blnc_sht_lst)

# 


