
def click_ad(ad):
    ad.clicks += 1
    ad.advertiser.clicks += 1
    ad.save()
    ad.advertiser.save()