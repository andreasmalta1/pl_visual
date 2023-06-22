from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings

from minutes.utils import get_num_matches, get_minutes
from minutes.plots import plt_minutes


def home(request):
    df_comps = pd.read_csv(os.path.join(settings.STATIC_ROOT, "comps_info.csv"))
    df_comps_mth = pd.read_csv(os.path.join(settings.STATIC_ROOT, "comps_matches.csv"))

    df_comps = get_minutes(df_comps)
    mth_comps = get_num_matches(df_comps_mth)

    graph_path = plt_minutes(df_comps, "Manchester-United", mth_comps, 10260, "comps")

    return render(request, "minutes/index.html", {"data": graph_path})
