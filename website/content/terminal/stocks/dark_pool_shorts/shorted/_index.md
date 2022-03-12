```
usage: shorted [-n NUM] [--export {csv,json,xlsx}] [-h]
```

Request a list of up to 25 stocks that have accumulated the most short interest. [Source: Yahoo Finance]

```
optional arguments:
  -n NUM, --num NUM     Number of the most shorted stocks to retrieve. (default: 5)
  --export {csv,json,xlsx}
                        Export dataframe data to csv,json,xlsx file (default: )
  -h, --help            show this help message (default: False)
```

Example:
```
2022 Feb 15, 11:06 (✨) /stocks/dps/ $ shorted
                                                                 Most Shorted Stocks
┌────────┬────────────────────────────────────────┬──────────────────┬────────┬──────────┬────────┬───────────────────┬────────────┬────────────────┐
│ Symbol │ Name                                   │ Price (Intraday) │ Change │ % Change │ Volume │ Avg Vol (3 month) │ Market Cap │ PE Ratio (TTM) │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ ECAT   │ BlackRock ESG Capital Allocation Trust │ 16.86            │ 0.13   │ +0.78%   │ 40765  │ 347083            │ 84300      │                │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ BLNK   │ Blink Charging Co.                     │ 24.75            │ 0.97   │ +4.08%   │ 354745 │ 2.357M            │ 1.044B     │                │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ HRTX   │ Heron Therapeutics, Inc.               │ 8.74             │ 0.22   │ +2.58%   │ 200853 │ 2.077M            │ 890.912M   │                │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ SAVA   │ Cassava Sciences, Inc.                 │ 48.83            │ 0.13   │ +0.28%   │ 430440 │ 3.047M            │ 1.954B     │                │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ ARCH   │ Arch Resources, Inc.                   │ 116.90           │ 3.64   │ +3.21%   │ 623213 │ 493427            │ 1.79B      │ 59.80          │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ EVGO   │ EVgo, Inc.                             │ 10.01            │ 0.27   │ +2.77%   │ 1.144M │ 4.419M            │ 2.648B     │                │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ BEEM   │ Beam Global                            │ 14.56            │ 1.07   │ +7.92%   │ 59466  │ 357145            │ 130.285M   │                │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ SDC    │ SmileDirectClub, Inc.                  │ 2.29             │ 0.07   │ +3.39%   │ 1.018M │ 8.748M            │ 886.831M   │                │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ BGFV   │ Big 5 Sporting Goods Corporation       │ 17.84            │ 0.52   │ +3.00%   │ 139821 │ 1.183M            │ 398.025M   │ 3.88           │
├────────┼────────────────────────────────────────┼──────────────────┼────────┼──────────┼────────┼───────────────────┼────────────┼────────────────┤
│ BYND   │ Beyond Meat, Inc.                      │ 59.97            │ 1.84   │ +3.17%   │ 480665 │ 3.702M            │ 3.798B     │                │
└────────┴────────────────────────────────────────┴──────────────────┴────────┴──────────┴────────┴───────────────────┴────────────┴────────────────┘
```