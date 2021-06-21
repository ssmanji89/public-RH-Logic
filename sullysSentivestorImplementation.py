dayOfWeek = date.today().strftime("%A")
hr = datetime.now().hour

vxxNow = ('VXX', info='last_trade_price') 
vxxYest = ('VXX', info='adjusted_previous_close') 
spyNow = ('SPY', info='last_trade_price') 
spyYest = ('SPY', info='adjusted_previous_close') 
mmtmNow = ('MMTM', info='last_trade_price') 
mmtmYest = ('MMTM', info='adjusted_previous_close') 

if ((dayOfWeek != 'Sunday' and dayOfWeek != 'Saturday') and (hr >= 10 and hr <= 17)) and (vxxNow > vxxYest or spyNow < spyYest or mmtmNow < mmtmYest): 
    sentipy = Sentipy(token=token, key=key)
    
    #AHI - Absolute Hype index / RHI - Relative Hype index / SGP - Standard Generalised Perception
    metric = "AHI"
    print('Metric:',metric)
    
    limit = 25
    print('Limit:',limit)
    
    sortData = sentipy.sort(metric, limit)
    trendingTickers = sortData.sort
    tckers = []
    looping = 0
    for ticker in trendingTickers:
        looping = looping + 1
        # print(ticker.ticker)
        tckers.insert(looping,ticker.ticker)
    lst = tckers
    l=1
    while l > 0: 
        sellCounter = 0 
        buyCounter = 0

        dayOfWeek = date.today().strftime("%A")
        if ((dayOfWeek != 'Sunday' and dayOfWeek != 'Saturday') and ((hr >= 7 and hr <= 8) or (hr >= 10 and hr <= 17))):
            print('::: >Start LIST----')
            for i in lst:   
                try: 
                    symbol = i
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)
                    oldChange = float()
                    time.sleep(random.randint(1,5))
                    change = float()
                    
                    print('> Start: ',symbol,'--')
                    
                    #sullys 'SMA' 
                    curClosePrice = float(0.000) 
                    runningMonth = float(0.000)
                    hourDay = [DATASTREAM]    
                    for u in hourDay: 
                        curClosePrice = float(0.000) 
                        curClosePrice = float((u['close_price']).replace("'",""))
                        runningMonth = runningMonth + curClosePrice
                    raw_Day3mo = float(round((runningMonth/len(hourDay)),6))
                    
                    if (hr < 9 or (hr >= 10 and hr <= 17)): 
                        print('Selling Logic')
                        if vxxNow < vxxYest and quote > (previous_close+(previous_close*.03)) and (hr >= 10 and hr <= 17) and (change > raw_5minuteDay and change > raw_10minuteDay):
                            [EXECUTE SELL TRADE]
                        time.sleep(random.randint(1,5))
                        
                        print('Buying Logic')
                        if (quote < (previous_close-(previous_close*.01)) and (volume > average_volume)) and (raw_hrDay < raw_hourWk and raw_fiveminDay > raw_tenminDay and change < raw_fiveminDay): 
                            [EXECUTE BUY TRADE]
                        time.sleep(random.randint(1,5))
                    
                    print('> END: ',symbol,'--')
                    continue
                except: 
                    print('Skip -',i)
                    continue
                print('::: >DONE LIST: Sleep for 2300 Seconds ----')
                time.sleep(2300)
        else: 
            print('Not Market Hours Sleep 300 seconds.')
            time.sleep(300)