def process_data(data):
    """Analyzes the data, looking for maximums.
    Returns a list of lines that summarize the information.
    """

#     revenue, numsold are lists of stats per entry in data
#     yearly is a dictionary adding together volume figures by year

    revenue = []
    numsold = []
    yearly  = {}

    for item in data:

        price = locale.atof(item["price"].strip("$"))
        sold = item["total_sales"]

        revenue.append(sold * price)
        numsold.append(sold)

        year = item["car"]["car_year"]
        if not year in yearly.keys():
            yearly[year] = sold
        else:
            yearly[year] += sold

    k_rev = revenue.index(max(revenue))
    k_qty = numsold.index(max(numsold))
    maxyr = max(yearly, key=yearly.get) # index turns out to be the key!

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(data[k_rev]["car"]), max(revenue)),
        "The {} had the most sales: {}".format(
            format_car(data[k_qty]["car"]), max(numsold)),
        "The most popular year was {} with {} sales.".format(
            maxyr, yearly[maxyr])
    ]

    return "\n".join(summary)
