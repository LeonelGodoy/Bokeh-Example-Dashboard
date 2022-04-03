
import pandas as pd
# Bokeh basics
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
from dashboard import _tab as dashboard_tab

policy_data = pd.read_csv("data/Auto - Policy Export.csv", low_memory=False)
# Create each of the tabs
tab1 = dashboard_tab(policy_data)
TABS = Tabs(tabs=[tab1])
# Put the tabs in the current document for display
curdoc().add_root(TABS)