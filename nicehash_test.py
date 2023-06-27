from nicehash import *
import time
from bokeh.plotting import figure, show
from bokeh.models import BasicTickFormatter, HoverTool, BoxSelectTool, BoxZoomTool, ResetTool, Span, OpenURL, Range1d, CustomJS, Button, DatePicker
from bokeh.models import NumeralTickFormatter, WheelZoomTool, PanTool, SaveTool, ColumnDataSource, LinearAxis, FactorRange, Label, Legend, LabelSet, Panel, Tabs
from bokeh.models.widgets import Select, RadioGroup, DataTable, StringFormatter, TableColumn, NumberFormatter, Div, inputs, Slider, CheckboxGroup, Toggle
from bokeh.io import curdoc
from bokeh.layouts import row, column, gridplot, layout

pprint(dir(private_api))
a = private_api.payout_call()
print(a)

tt = {
  "list": [
    {
      "id": "a7fa1cff-8e6e-44d7-a2ed-957c19e64ae9",
      "created": 1654690408708,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006461",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "6db40bf7-87c2-48aa-b487-d6dcbd6da448",
      "created": 1654675715234,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006230",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000125
    },
    {
      "id": "23998e76-f778-4dd5-828c-a6c4856b530e",
      "created": 1654661502287,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006440",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "554410c7-7dcc-4398-b404-7ebb9f60e1e5",
      "created": 1654646960480,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006823",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "8c53c168-c588-4c8f-b1fb-80312389631d",
      "created": 1654632748593,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006338",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000127
    },
    {
      "id": "17aa5bea-bb82-411e-80c1-389235c3894f",
      "created": 1654618171816,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006495",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "860484be-de01-4b46-bbee-8f73ff713072",
      "created": 1654603955673,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006477",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "b1b5804c-24b5-4585-ab73-c2d9c385ed15",
      "created": 1654589574787,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006486",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "b923ce8f-9c37-4484-a979-ff32d2e358a0",
      "created": 1654575155303,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006666",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "f079978f-148a-4010-a32d-2ecf5e57f20a",
      "created": 1654560726631,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006300",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000126
    },
    {
      "id": "149fd179-f9fa-4ed4-8da0-54d666521ee4",
      "created": 1654546361266,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006444",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "9f3a6b0f-cd1f-4e4e-afc8-1cea3a6f788c",
      "created": 1654531975175,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006349",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000127
    },
    {
      "id": "dd0ffe8e-736f-48e6-a8b5-b1bf3c0e35f1",
      "created": 1654517503551,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006721",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "93ccdfa5-3dd5-413d-a7da-91fa56a15552",
      "created": 1654503189945,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006506",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "7cc356c1-da91-4dd8-9bfb-3f0c920ba94f",
      "created": 1654488680924,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006709",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "c4cec0ca-97f2-463a-806e-eb3868ce6a65",
      "created": 1654474348030,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006543",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000131
    },
    {
      "id": "87488b4e-2206-438a-8bd8-47f1763482cf",
      "created": 1654459884519,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006669",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "351995c3-b0df-4eee-b6f9-a4926e8e8872",
      "created": 1654445546077,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006467",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "57504c4c-6b78-4a72-bf3e-eae771cbd5d8",
      "created": 1654431073572,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006532",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000131
    },
    {
      "id": "cdc7ca52-9526-488b-a676-8a5c30eda866",
      "created": 1654416813239,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006607",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "1cb70f6a-1585-46af-8f65-7bc654723bab",
      "created": 1654402334755,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006646",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "7a3399a2-4c16-40e4-bb70-63d8e04eff4b",
      "created": 1654387954472,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006738",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "ce992460-2319-4ca9-8344-30369b1e8cbb",
      "created": 1654373415924,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006405",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000128
    },
    {
      "id": "48446b3b-92bb-4039-8ef4-05bc22382489",
      "created": 1654359060850,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006329",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000127
    },
    {
      "id": "1279a5d7-6e11-4af5-89cd-5ff6d1ac145f",
      "created": 1654344491031,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006111",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000122
    },
    {
      "id": "4dc7a3a7-d165-4893-b4a0-9cba30d06207",
      "created": 1654330254521,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006126",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000123
    },
    {
      "id": "2e1b0251-956a-48c2-807f-5ae7f5f07fb7",
      "created": 1654315984460,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006555",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000131
    },
    {
      "id": "191276a3-ee9d-4346-8ca0-0232422d6156",
      "created": 1654301448671,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006807",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "02add07f-1849-48ae-b16b-85e31f074bf7",
      "created": 1654287136834,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007031",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "f4cccad1-3a61-4f8b-b2bf-0f63b55d211e",
      "created": 1654272724501,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006879",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "8dd5c958-7937-4390-a843-cac553d47c0c",
      "created": 1654258404772,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006660",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "6bbbdd0f-274b-4497-a52d-22ccb747100d",
      "created": 1654244009651,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006796",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "948cc6fe-f4ce-414d-89ea-da0e8a6f7853",
      "created": 1654229604150,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006692",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "81854eda-fd38-44b4-b48b-a99b9fd8d39a",
      "created": 1654215156243,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006890",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "f0ea15ec-a4f8-4d21-8dfb-2f97a0f287b7",
      "created": 1654200786218,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006892",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "fa14878c-bc38-48fd-bbd7-c2589049df09",
      "created": 1654186357214,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006713",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "ef4f52f8-6fe3-4932-bbe3-29c0a19ad74a",
      "created": 1654172040271,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006875",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "15c66396-2834-4202-a8f6-87fe9b59db32",
      "created": 1654157637479,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006578",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "2dac147d-2fef-4a85-8dbf-ff25776e43d3",
      "created": 1654143165503,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006879",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "b7577f20-cf1c-45ce-83bb-c826b3192ec9",
      "created": 1654128757817,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007088",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "18a24738-9325-4f43-bde9-37fa2bd13cc3",
      "created": 1654114311124,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007285",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "4325cbef-4e51-41ec-81aa-98ed5e984816",
      "created": 1654099977699,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006901",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "21b631f8-ac41-46a6-bfdf-44a10172b562",
      "created": 1654085604855,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006819",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "ab76e241-a7da-436f-9d2f-c93a49dfa640",
      "created": 1654071133969,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001738",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.5e-7
    },
    {
      "id": "ec8319de-6d99-4372-a025-20dc44a9e21d",
      "created": 1654056796434,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001427",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 2.9e-7
    },
    {
      "id": "adeccb27-5afc-44a8-baf4-bed695e04b33",
      "created": 1654022212869,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "38e2ac38-83fd-4afc-8180-7d779eb28480",
      "created": 1653999353216,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007058",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "7ec2dead-4c8c-466a-8824-537d81f261f3",
      "created": 1653984709631,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006905",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "2969c2e4-0282-480e-a5a0-0417d0112869",
      "created": 1653970142979,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007313",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "1e585752-8814-4d9e-bf37-c45918cf3b02",
      "created": 1653955549079,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006831",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "a4d5c9d2-a90a-4b66-a5a6-2b239ef0f65f",
      "created": 1653941519058,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007238",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "2b868120-db64-4774-9cc5-76a191a9cfac",
      "created": 1653926695695,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006061",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000121
    },
    {
      "id": "a7c389ae-df08-4d34-8274-69d7e9937eef",
      "created": 1653912874336,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007063",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "810f0a9e-e252-474e-9ed2-9745dbd9f76f",
      "created": 1653898239569,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007088",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "fbcc47c3-c335-4daf-b897-89c03c2780ab",
      "created": 1653883923959,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006864",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "4128f7f8-890c-460c-9397-b8346c51b4d0",
      "created": 1653869401796,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006808",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "ff22c4cd-6c34-4652-b154-96c9dc157c26",
      "created": 1653855236647,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006939",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "f9ae0bd4-f009-473a-a787-3eead958696d",
      "created": 1653840514344,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006831",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "1d9f141d-edd9-4551-aeba-8019a0b1e716",
      "created": 1653826474220,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006930",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "e3099a8e-d9fa-4c74-800f-7dd229110312",
      "created": 1653812064561,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006906",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "e9069293-704e-4ebd-8137-c0ac17a8d6c6",
      "created": 1653797561916,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006832",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "f535cbf7-2108-46ef-bc24-5ad786c59e53",
      "created": 1653783030807,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007061",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "4e4005a8-d700-4419-a790-6ab13c8969a8",
      "created": 1653768667229,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006857",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "c23aec08-9407-436b-883b-7c6a7fbef798",
      "created": 1653754400703,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006738",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "7037f0e0-c930-45de-ba15-a443a26d3e8d",
      "created": 1653740053355,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007207",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "d5932a4e-f601-437b-a47c-725857210e66",
      "created": 1653725415980,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006900",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "d425ad4b-4430-47f6-b447-7966ab817fe0",
      "created": 1653711190703,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006921",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "55eebbcc-9394-4d14-b8c2-9fae681a0937",
      "created": 1653696775037,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006621",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "a3152995-64c3-4deb-a54c-c8d7594c0c2a",
      "created": 1653682364143,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006775",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "af407f1e-7344-4a68-9b08-3239a222e76c",
      "created": 1653668044470,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006827",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "e08c2e1f-e09c-46f1-99b6-40a937a2c997",
      "created": 1653653686754,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006649",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "4843046b-fc9c-4424-9ff9-986569c68ff7",
      "created": 1653639313595,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006985",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "27f1f21c-ca46-4eaa-b643-7fd79c92bb4f",
      "created": 1653624789199,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006969",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "17508de5-2f1d-43d7-a14f-774a3bab1448",
      "created": 1653610395240,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006960",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "63c2d918-924a-4316-8d5c-1936932e96b9",
      "created": 1653595927590,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006877",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "d865aeb1-68ff-40f8-bc66-373e63f3d46e",
      "created": 1653581670452,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007449",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "e8382398-3414-4538-a82c-01f5131e6ad1",
      "created": 1653567251250,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007243",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "3b6126d7-271d-493a-9f32-788d8c5a1f98",
      "created": 1653552871467,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006036",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000121
    },
    {
      "id": "d2b355f5-4a13-4f05-a0c9-148fb90f2cb6",
      "created": 1653538490553,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006698",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "bea7b039-e021-4d33-85bf-6b49a8573915",
      "created": 1653524011042,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007231",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "06f6853b-eb63-43ca-b87d-c471d0847194",
      "created": 1653509555017,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007414",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "394ccde6-6f7b-4b2d-8a49-6a488bb1e4f8",
      "created": 1653495257028,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007206",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "ceb648c7-72b8-4e58-bbcc-9b2696200e25",
      "created": 1653480862106,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007466",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "f0747296-dbab-46bc-81cb-2f58a6705204",
      "created": 1653466493889,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007312",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "890baff0-9cd5-435e-b7a2-756b893f07b7",
      "created": 1653452037398,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007744",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "fccd5929-1dc0-468f-987a-33c322c4d8f9",
      "created": 1653437332363,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "4c4abcd4-ea1e-4524-a39b-2a5b32d72e3a",
      "created": 1653423273840,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007370",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "6ffaf7bb-9252-423d-9c68-fa848afa6bbc",
      "created": 1653408939924,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007455",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "54456852-4c8f-436a-aff4-18d9d4402ab4",
      "created": 1653394393258,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007357",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "7e863c36-db1a-4993-a351-ed35a8938543",
      "created": 1653380065397,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007445",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "2a3684ac-f5b4-4bd4-ad4b-8f77dcb801f0",
      "created": 1653365648160,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007349",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "a7130cce-3f5d-4ed9-8a56-d39a39e3326a",
      "created": 1653351174606,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007354",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "c4322361-bc53-4256-85e2-2087930f2ff7",
      "created": 1653336883157,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007626",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "a5868822-36c6-47af-a929-2c61dca7506d",
      "created": 1653322494324,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007340",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "e77baf65-0553-451c-b207-26b5ca03f91c",
      "created": 1653308044650,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007669",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "a1e1dcab-9c51-4c02-91bb-134703d338e3",
      "created": 1653293643074,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007652",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "3789ecea-4f59-4005-bf8e-5c08c5e3a081",
      "created": 1653278942671,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007655",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "e0782605-0cf7-4bd8-8824-67d0bf21695e",
      "created": 1653264780518,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007320",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "27e16b65-325e-4d4a-9978-b5a29948d56e",
      "created": 1653250447754,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007484",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "9054008c-e5e6-4144-ab9b-5ba9b09199ba",
      "created": 1653236060391,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007530",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "883e2622-741a-4588-84af-5f41e3dba0c5",
      "created": 1653221451958,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007340",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "1802485d-fd74-404e-8e97-204d96c8acc3",
      "created": 1653207255802,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007427",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "6f273d9f-d206-465a-be00-d0bacbe58c4d",
      "created": 1653192848086,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007275",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "382db48a-0520-4fe4-88f7-ca7992036309",
      "created": 1653178348506,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007419",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "943cda51-060d-4b83-8b5d-f9ac9f344a71",
      "created": 1653164053907,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007295",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "19dc63e1-1774-4d88-b745-4b70473e7499",
      "created": 1653149679615,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005744",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000115
    },
    {
      "id": "12963d04-3bf1-4b89-8321-7ac441b72e37",
      "created": 1653135071137,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004098",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.2e-7
    },
    {
      "id": "0a5e3163-cdbb-4f4d-a77d-c2f23634888f",
      "created": 1653120820695,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003883",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.8e-7
    },
    {
      "id": "71762fc2-f0bf-458a-8460-e98afcab2874",
      "created": 1653106450869,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004712",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.4e-7
    },
    {
      "id": "85775f63-e79e-47d0-b1c9-a84b8fa8b7a3",
      "created": 1653092018260,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007026",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "ae108bb7-108e-442f-b1dc-2a2d6848ea2c",
      "created": 1653077690045,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007472",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "61b094fd-37e3-4a8c-b600-9412b4766edd",
      "created": 1653063131909,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007370",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "15da1bad-0fa6-4fa4-a215-22e06b9590ba",
      "created": 1653048876212,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007428",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "6528ae42-072f-469e-9cd6-5364b0cfed1d",
      "created": 1653034485984,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007383",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "19fb1860-ece7-41c5-ac42-ce581c8e3bf0",
      "created": 1653020117012,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007251",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "bd232282-e222-43e4-87d7-2a46e9f4e5e7",
      "created": 1653005666351,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007333",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "5d60a3ee-26df-4d2c-9554-86912c64eaf8",
      "created": 1652991249732,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007421",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "9574486c-6d72-4452-89f5-1eacbe1d6c01",
      "created": 1652976902385,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007564",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "43672bf1-a131-45c9-bc19-36e1eac6bedb",
      "created": 1652962509617,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007500",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "02610c1d-fb83-4162-b8b0-b6b6a5c84948",
      "created": 1652947964181,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007314",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "49acc0a5-fb91-41b8-85e3-7566d97bed16",
      "created": 1652933738598,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007213",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "ca66de57-fdb0-487f-a959-042a4dee6071",
      "created": 1652919223727,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007362",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "ca1aa1a0-dbd2-4724-927e-68161985d440",
      "created": 1652904637798,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007577",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "dac54bf8-aa4b-424e-bb34-7f038819e726",
      "created": 1652890207714,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007744",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "fb18fa19-22c7-4dad-920a-e2398c821bc2",
      "created": 1652876068651,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007496",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "1bc1a28f-9b4a-4334-8cab-b65498c193ea",
      "created": 1652861681211,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007595",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "d8c38700-f42e-4cc7-81e1-a84221c79282",
      "created": 1652847027512,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007614",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "61fcd29f-32db-42bc-bd57-35246e59ce78",
      "created": 1652832824980,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007634",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "6001b16e-5bbc-470b-a389-498760291940",
      "created": 1652818505343,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007955",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "47bf009b-6643-4402-97fc-a16fbb62eee3",
      "created": 1652803790201,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008048",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "96a48aa6-f7f3-420a-9e00-75642793f69a",
      "created": 1652789716728,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007666",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "06986f2c-94e7-4c52-a79b-842e6a4660f0",
      "created": 1652775047239,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007877",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "730887bc-5c6b-464a-93cb-be908f6a3a7f",
      "created": 1652760818519,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "404ab1c7-446e-4f11-b3a1-f7c2f7debd78",
      "created": 1652746441820,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007389",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "783971fc-f270-4b63-ae3f-5add341a6a33",
      "created": 1652731779790,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007849",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "0a626cef-f15d-415d-8bf2-05229bdcea9e",
      "created": 1652717410499,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007525",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "d0429485-516a-4ef4-9724-f98598ca4bcb",
      "created": 1652703055754,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007775",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "fa3a86c9-f14e-48d0-b926-f22e2d26e018",
      "created": 1652688846996,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007739",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "43e66270-37a7-44db-aab4-675a39f02275",
      "created": 1652674263999,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007920",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "5783c7ed-6b44-42b8-a73d-ff963d9e234a",
      "created": 1652659847899,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008077",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "be89c722-47b3-4104-87d3-df501db6a3fc",
      "created": 1652645433835,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007919",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "551c98af-5a6f-4dd9-a250-67c07d48777a",
      "created": 1652631080928,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007784",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "19b362d7-3aaf-47c3-bcc7-6023f1151357",
      "created": 1652616976854,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007467",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "19af2fc4-b9b7-4fc5-86ce-44f3932a5179",
      "created": 1652602300978,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007704",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "adf7538a-ec9f-48dd-a479-ad7e4bf73bd4",
      "created": 1652587857922,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007565",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "6c7a83bd-810a-4322-8539-f1daaa486b2c",
      "created": 1652573645928,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007808",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "2a952148-140e-4e16-aabc-088a5d718824",
      "created": 1652559099802,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007926",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "c12ce65e-a1fc-476e-8824-67ddaf74dffc",
      "created": 1652544871289,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008393",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "c2e9cc66-4a39-4e58-b1b1-834329ef9eb6",
      "created": 1652530479459,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008299",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "18dcc280-c72a-4e98-ae4c-6b3f06b12e1a",
      "created": 1652515927303,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007847",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "42d89d60-c35e-4f8f-b303-3312d702b61b",
      "created": 1652501389148,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007600",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "25e38a38-5d55-4b94-91bb-ba96316823f7",
      "created": 1652487215567,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007397",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "164da88b-2ae9-49c7-b26d-fce064fc69dc",
      "created": 1652472671686,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007791",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "f0c2572b-c31b-45fc-ae41-241afc145cb8",
      "created": 1652458284782,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007950",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "72a8929e-9170-4fc5-8db0-9c6f913c5d10",
      "created": 1652444057320,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007974",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "5c028b29-586f-457b-bda1-ee39e534255e",
      "created": 1652429683244,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008257",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "30239ded-bcdd-4c5f-a527-6e6d2e8a7c49",
      "created": 1652415299780,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008222",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "135ef7f3-8c49-4e0a-9060-81c56d686dae",
      "created": 1652400895864,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008402",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "13bd5fb9-bd4d-47af-90e3-e6f9c4e508a3",
      "created": 1652386457523,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008783",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "d4a5fcbd-f6f7-4707-83b7-23d79b0d9814",
      "created": 1652372127084,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009295",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "94265922-25ce-479b-aec2-5736c9f3960c",
      "created": 1652357812874,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009467",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "11f124ed-8aa3-4ed3-8a7c-6a61e0eab1fa",
      "created": 1652343405649,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009329",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "852dcc37-d39d-4be8-b7e6-745d52207652",
      "created": 1652328844315,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008609",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "3e205104-716c-4255-97dd-2ce00dac34e9",
      "created": 1652314280205,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008480",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "6968599c-ad06-4899-b625-7ee0c270b991",
      "created": 1652299711635,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008573",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "c8406d3d-3303-437a-bc82-f0b70fa551a6",
      "created": 1652285611160,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009466",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "39bcf942-71a8-4357-96b2-15bade942cf2",
      "created": 1652271269160,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009042",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "288eeb23-6e12-4cd0-a460-80edfc75dbc2",
      "created": 1652256973660,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008859",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "2f2a964a-de7c-45c7-a8ee-6cc4b34aba83",
      "created": 1652242565748,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009023",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "eb73bd9a-9fa5-4409-b721-9055a8021d7d",
      "created": 1652228060010,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008637",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "ebc06745-d90c-4f90-8dcf-ae3515c706b5",
      "created": 1652213833496,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008647",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "fa671a81-b356-4244-a3f5-53e82ba0aa74",
      "created": 1652199189436,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008763",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "2be01bcb-93b5-48f5-abfc-eab0ec1ed174",
      "created": 1652185064477,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008854",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "eff55583-596d-4b8a-9a89-baedac115314",
      "created": 1652170530419,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008877",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "a9f828cb-b3d5-4234-9dc6-0736311a91c0",
      "created": 1652155694583,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009142",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "6a73a853-49d9-461a-9e80-5b70eb8698ac",
      "created": 1652141374078,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008622",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "17496a3f-f696-4243-991b-50dee3476d32",
      "created": 1652127445220,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009189",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "1d073522-e91c-4dd0-a6af-c0a894121603",
      "created": 1652112879731,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008315",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "4ee89fd9-efde-41d6-99e9-a6423ddb7128",
      "created": 1652098564985,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006135",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000123
    },
    {
      "id": "49c71ff5-b66f-46ce-9a1a-3f0b2522a291",
      "created": 1652084021313,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004604",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.2e-7
    },
    {
      "id": "97abb321-8c64-4c01-aab5-1df69c238cf7",
      "created": 1652069715092,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004609",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.2e-7
    },
    {
      "id": "e6c19864-629c-4ff9-8797-a9e517554944",
      "created": 1652055320248,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004494",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9e-7
    },
    {
      "id": "952581c5-f0f9-47fb-8054-26be58ca1c51",
      "created": 1652041024810,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004816",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.6e-7
    },
    {
      "id": "e8366475-6e41-423b-b196-d636ef7db88c",
      "created": 1652026538618,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004538",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.1e-7
    },
    {
      "id": "a5ea2794-6f92-491d-ba85-d68f25c1955f",
      "created": 1652012210384,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004854",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.7e-7
    },
    {
      "id": "acaaf27c-7fd4-405c-9173-df50996b839d",
      "created": 1651997772635,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004665",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.3e-7
    },
    {
      "id": "5ed134f1-b8b8-4837-90b9-836e43c80e12",
      "created": 1651983357602,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005413",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "524827ee-cd45-43c0-a171-62b1033cb46f",
      "created": 1651968918309,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008506",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "c0e7a50b-647a-4e84-ab31-8e13c9823ba6",
      "created": 1651954524885,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008563",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "97c4fcd9-8680-4c54-8477-83787c6713dd",
      "created": 1651939733967,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007611",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "6fbc5724-6466-4c99-a413-38f559fbba99",
      "created": 1651925818255,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007995",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "aa9f6d7c-ebad-49d1-be7c-c0dfbde93ce0",
      "created": 1651911352857,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008122",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "d3812512-87f8-4e62-b0e3-723fc36e569b",
      "created": 1651896891331,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007824",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "04c66b9a-89c5-4fc4-ae33-015fd164397e",
      "created": 1651882421018,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008251",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "4acf2b0f-07f3-4ebf-a387-5fcf291355a8",
      "created": 1651868149237,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007981",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "7b459714-af87-43f1-886e-231678ec755b",
      "created": 1651853731717,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008634",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "a8caecb0-b5f1-4021-907a-6c6cd728582b",
      "created": 1651839351289,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007915",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "d4cf6055-d731-43a6-92fa-537a653a7183",
      "created": 1651824885372,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008038",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "da09b6bf-1150-4e40-b61a-f8ae7aed1efb",
      "created": 1651810563305,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008130",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "8f21dd01-235e-4349-b154-31624b3b4ce9",
      "created": 1651796057583,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008112",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "112e51f1-de30-4ec4-a7f9-bc0545b6511d",
      "created": 1651781737977,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008108",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "069ac449-8e8e-4ab4-8585-02608ec8bbf6",
      "created": 1651766973054,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008163",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "d40510b9-6224-4cb2-9b56-0121889b114d",
      "created": 1651752932105,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008199",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "142cf5de-6985-480d-aaf1-b486d0bda853",
      "created": 1651738465119,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007675",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "8d54b02b-d711-46e9-a40e-3f04860775c8",
      "created": 1651724277473,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008539",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "b2dd0ddb-2c91-4b04-8b0b-d07c3c0cc7e0",
      "created": 1651709691172,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008053",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "70917320-eacc-4f03-bcbf-aba6121469f8",
      "created": 1651695357391,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007566",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "f6e9aaeb-4ce1-49ed-b663-b65e127c4cfa",
      "created": 1651680951178,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007682",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "1d8ce371-4dee-4a10-b8a1-675b3c2e00ea",
      "created": 1651666348408,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007852",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "9bed5a66-f94d-4e5e-9078-1e3df5b96bf2",
      "created": 1651651405538,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008046",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "1b19eda1-691a-4186-9f09-4da8ea895fa7",
      "created": 1651637535112,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007800",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "9ef4da3a-466c-47a6-8999-650900c50096",
      "created": 1651623218624,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007409",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "ff6aa7d3-a3ab-4a69-afa2-8200e9844194",
      "created": 1651608917904,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007746",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "ef396994-5a77-41c0-bbe4-ac55c9005175",
      "created": 1651594496045,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007734",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "c708d886-0054-4c54-962c-fb20566e8ebf",
      "created": 1651579847634,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007828",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "58637ba4-98f3-49e2-b6c9-62cdc9c3b3e3",
      "created": 1651565400096,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007618",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "d0aaa8f7-ae03-4a8d-a72b-77fcd3679d9c",
      "created": 1651551108908,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007945",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "9ac32e4a-3784-4ab6-9127-67812bce5893",
      "created": 1651536741939,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007573",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "bb573b08-6f67-4dcc-acb8-6e95e029f2d5",
      "created": 1651522399838,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007476",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "6344837b-eba9-4a25-a9a9-5b1f4510abf5",
      "created": 1651508063267,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007858",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "06cf914e-50ab-408b-94e0-f3f0e4f26448",
      "created": 1651493747903,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007726",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "87d5d7c0-6945-4a23-9d92-47ba4a098d16",
      "created": 1651479135909,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007709",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "6eeb0808-aaf3-482c-a719-8a058efe39ec",
      "created": 1651464960807,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007809",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "8adf159d-62ca-47fa-90a9-866d92c5feb6",
      "created": 1651450251091,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008849",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "ed61f645-d263-4789-a14d-2208145c29f0",
      "created": 1651436008951,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008092",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "06bc99dd-532e-45cc-96b4-377c5ee27d3e",
      "created": 1651421517586,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007634",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "07c6243c-f70a-4316-ae3c-c9a1bb37cae6",
      "created": 1651407295443,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008025",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "37e577c1-08c9-40b3-b351-1c557c67035c",
      "created": 1651392600162,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008348",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "d8973a39-09cf-478b-b5a6-a893eb470886",
      "created": 1651378604606,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00018112",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000362
    },
    {
      "id": "577deb75-4726-4255-83c4-04e91093dd14",
      "created": 1651363974001,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008231",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "0446f7c8-2ed6-4979-a320-a29e7499f345",
      "created": 1651349373168,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007887",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "c0183276-8525-4ee6-acde-17eefe0f41d6",
      "created": 1651334930534,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007873",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "8d8e795b-f0d4-496a-8338-d06d5ad3b6b7",
      "created": 1651320508400,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007965",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "eee0b208-35ea-444d-9c67-417d8150343a",
      "created": 1651306252036,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007904",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "be89ffbc-26c0-41ed-a774-7ba58603cb6d",
      "created": 1651291743407,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "fc3da905-d677-411d-834a-eafb5cabefaa",
      "created": 1651277548163,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008224",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "884b2c14-27c4-4537-8191-b70bf512cab9",
      "created": 1651263271145,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008505",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "549988ca-2fc9-4912-97d5-ee14f46a67f3",
      "created": 1651248932020,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008279",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "1b113acf-1f79-4773-a7bb-66647e6ae13c",
      "created": 1651234464082,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008181",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "925fe10d-d4d4-43f9-ad24-1093d7b6a4df",
      "created": 1651219756316,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008417",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "58049607-5361-4d65-914b-1d681b883f5f",
      "created": 1651205816064,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008371",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "f6470789-91f2-4c14-98a7-1a057740e070",
      "created": 1651191103656,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008378",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "42e8b7ef-81ac-47f5-911f-7940913ba372",
      "created": 1651176939290,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008162",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "bc7070c1-b73f-41b6-80ba-47da55867ee2",
      "created": 1651162519451,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008025",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "06144b98-e4ce-4152-b466-57ae618c4019",
      "created": 1651148256580,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008122",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "1e3595bb-e0fb-4e5b-a3e7-dba969f9251a",
      "created": 1651133521181,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008299",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "d71e7ad4-ee77-4f7b-a27d-25bc7dc037e2",
      "created": 1651119217252,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008528",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "4f0165b1-65a8-4a5b-9098-2bec52e5d2ee",
      "created": 1651104524375,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008367",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "16be95d2-75c6-44f8-a209-8f19b51f9002",
      "created": 1651090548108,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008458",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "c144c540-2167-48e3-8ff8-54e083822e35",
      "created": 1651076039866,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008359",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "f8fb530b-b3b9-4b00-9ecd-10ffa7f59073",
      "created": 1651061541225,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008398",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "764aa206-74db-486f-870b-538816bc2df0",
      "created": 1651047102593,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008257",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "261b243b-93f2-4cfa-b9ae-d59e79d134be",
      "created": 1651032871391,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008426",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "ef6cc252-0c0f-4d12-aa2e-6b5b8ec15d22",
      "created": 1651018459125,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008621",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "4a0c0af9-93d2-4e08-8320-86603ca95e4c",
      "created": 1651004015618,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008203",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "2b1e0749-2bce-442c-9eac-dbced7d66315",
      "created": 1650989750898,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007841",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "3d630624-604a-40ab-b1a0-a6783c23017e",
      "created": 1650975109935,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007741",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "37c0fd90-398a-4f18-b810-4560cdc5e395",
      "created": 1650960644024,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008087",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "f2976f0c-6e0b-4728-805c-4458363d3e13",
      "created": 1650946495633,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008106",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "e1e62d4e-8439-4761-92b3-e7fb6e9484d2",
      "created": 1650932061526,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008267",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "01f4d64b-2b1f-4aa9-a536-3cb8aa1902ed",
      "created": 1650917532702,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008589",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "209dc6e9-a16d-4870-b558-8b97cfb05ca3",
      "created": 1650903255353,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008089",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "bf9fbeba-77da-433b-b03e-5e2be020c291",
      "created": 1650888948066,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008134",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "48f7dd57-cb1b-466b-85c2-93abeaf5fed2",
      "created": 1650874519486,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008042",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "caecbaaa-987b-418a-bdcb-ba7892849504",
      "created": 1650860058735,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008256",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "c7d74155-6165-4584-a076-3b3ee9f687c6",
      "created": 1650845527529,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008143",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "6aafaa68-db80-48cb-aa15-0a9149ac9b63",
      "created": 1650831311224,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008295",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "7da3fd1c-8f8e-496c-9a78-57c4624217b8",
      "created": 1650816725143,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008069",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "fe459caa-f2a0-48ab-94bd-bcfcd8a0bc44",
      "created": 1650802472070,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007825",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "2b1e5583-ddad-42a9-9eba-fca3bd0c2b13",
      "created": 1650788109677,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008024",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "1f2dc2c0-f3ce-4a7e-8e3f-7d280d299a89",
      "created": 1650773496884,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008286",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "041e4fa9-d04f-44a7-9b98-d5cef4e4d20b",
      "created": 1650759286645,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007811",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "67ec3318-d053-4453-8b1c-91aba0ea7802",
      "created": 1650744966530,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007837",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "e6d679da-28b3-47f7-bb8f-fc175b9b8277",
      "created": 1650730364021,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008257",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "830f1cf7-3b2a-4fa4-b9e5-7f35d85d3a45",
      "created": 1650716133500,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007993",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "2578df3e-5180-4884-8655-dfc5a944047f",
      "created": 1650701684803,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008354",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "6f57f2f7-a13f-4e8c-add1-1862a2895f6d",
      "created": 1650687398636,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007891",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "7a4c28e8-0287-4a4c-b85b-48bfdb8e0a8b",
      "created": 1650672868508,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008245",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "d22a163e-9a39-4435-9ef1-530e2ee0df58",
      "created": 1650658517429,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008394",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "79e08e13-7a28-4cab-8162-5a2e1761456a",
      "created": 1650644011658,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007966",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "a89570ce-5db2-4632-a7b9-a1b9f007656a",
      "created": 1650629269252,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008669",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "eda874e4-45d7-4657-8b0d-c241490dc8b3",
      "created": 1650615220085,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008213",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "1717cc74-f445-4f89-b94f-5bf1731ad84a",
      "created": 1650600922094,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008405",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "cbad2162-2f0d-40e8-8411-432d62dd27d9",
      "created": 1650586500090,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008022",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "de862ca5-a038-4aa5-b366-570cdb216492",
      "created": 1650571934734,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008504",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "aa77ef07-e2c1-4294-9684-caa5e1c2c089",
      "created": 1650557615039,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008147",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "a57b5ede-bf4d-4d19-af92-4830a544e2be",
      "created": 1650543478254,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008227",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "c62ac535-31b7-41db-b834-5c8dd8d3b9a5",
      "created": 1650528885267,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008098",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "48388212-c41b-4583-9920-ec572e605e2c",
      "created": 1650514564718,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008187",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "732a0822-233f-4009-9ffa-699d003bd3bd",
      "created": 1650499930985,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007992",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "19e933cf-ddc1-4bd3-91ab-c4a3a7e3b5ac",
      "created": 1650485801193,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008583",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "feb73001-cd7a-4d8f-b704-e21a7b6b461d",
      "created": 1650471174563,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008492",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "426faf42-b44f-46ee-b149-03d25479dc0e",
      "created": 1650456887278,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008517",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "e04b2429-24b7-4b99-8dbb-14102b2447e2",
      "created": 1650442678741,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008594",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "20d5e54f-5790-4c6b-a405-ee5acc08aac9",
      "created": 1650428185717,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008050",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "d00c8a6d-e274-4c67-b227-da2219f64152",
      "created": 1650413586580,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007841",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "47d8fded-cba3-45a3-a4a9-095d6ba8023a",
      "created": 1650399369946,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008122",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "76c5ba56-85a1-4be2-8276-0828ace68048",
      "created": 1650385063703,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008556",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "5e2144c6-e2f8-4b27-b0f2-2c5906683a50",
      "created": 1650370601323,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008189",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "79799330-f88c-4967-92c9-6512ad789c1d",
      "created": 1650355890172,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008321",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "b49c474e-7ea5-4c37-bbbb-075b389d1c5a",
      "created": 1650341417704,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008184",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "82cc3b9c-7d2d-4e5b-8915-fb1a3fe83fb0",
      "created": 1650327005845,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007998",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "ea609959-b2c5-4ce7-b47b-aa153840b7ff",
      "created": 1650312530908,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008334",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "e70879b5-9e73-4d0c-b9b3-c1dc4491b015",
      "created": 1650298255036,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008133",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "e8dded22-1f93-48ac-9337-80908bc8f0a0",
      "created": 1650283970223,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008121",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "b147d0dc-b676-4f41-8a6f-c4dd32acf833",
      "created": 1650269377455,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008309",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "ec5eebb7-2959-42fa-bb12-128326bb9f94",
      "created": 1650254997466,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008482",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "84ce5559-5d6d-48f0-b9d3-225f240c6e2d",
      "created": 1650240523417,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008539",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "7b9be54d-758e-4f7f-aa11-ab7e68b1643e",
      "created": 1650226330314,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008456",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "d52f7bbd-7353-4ec7-8942-7904f573ee52",
      "created": 1650211902980,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008382",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "7a1def6d-5e89-4085-9455-f1e89adffd4f",
      "created": 1650197613560,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008348",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "16d65fe9-b32e-42e4-8c07-e83c744268c1",
      "created": 1650183065129,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008430",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "0d3c2333-fce8-4dc2-bbae-2d066b166463",
      "created": 1650168631090,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008462",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "16e490d6-6c41-40b4-9ec5-fba758bd789a",
      "created": 1650154194634,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008417",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "e433bfdb-5754-4dc7-ba22-7e4b7d226dde",
      "created": 1650139734570,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008803",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "bb57c096-333f-4b2e-98dd-7684ef7156f2",
      "created": 1650125381247,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008675",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "3b9a0743-065b-45fa-8735-877e1e992e1f",
      "created": 1650110965603,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008481",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "0c91b63e-ef0c-4494-bfcc-20268e0d8475",
      "created": 1650096744945,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008336",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "4da3d9f5-98c2-4eb5-88a9-59405f49635b",
      "created": 1650082395975,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008228",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "27908cfa-5272-4b43-b4e7-0ee957b48a8b",
      "created": 1650067834538,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008049",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "897cc662-1feb-4cf2-bc08-02d01cc4f36c",
      "created": 1650053296050,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008662",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "67d957ee-c161-4f72-aa32-d52aa0d44ba6",
      "created": 1650039421734,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008648",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "f1a4488d-fde9-4ba3-8bb1-359abc661b30",
      "created": 1650024786108,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008654",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "240a6466-eccc-4f5b-ae7d-e0e9f4ba6bd4",
      "created": 1650010300064,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008472",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "73528fd0-49dc-42b0-9421-c336da6f23aa",
      "created": 1649995886524,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008437",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "a82e40bf-e01c-408a-9310-ebdec0b8da5a",
      "created": 1649981225509,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008613",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "0afaa125-3ec7-472d-94ab-83e5386081ea",
      "created": 1649966802817,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008228",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "ac76a688-e44d-4858-9ef4-b7d2740be748",
      "created": 1649952786239,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007109",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "fb274ec7-f78d-454b-be7f-315e05df5478",
      "created": 1649938193908,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007707",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "830ec23d-60c8-496b-b358-d58dcdee06f3",
      "created": 1649923746388,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008106",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "daf9cbfe-be15-4a3d-8ae5-251cd8642fb4",
      "created": 1649909288664,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007972",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "8c0357fd-6ebc-47d2-b796-5b9ca22b4ff7",
      "created": 1649894947397,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007037",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "e4bf6899-3ff3-4961-ac27-892caf11a98f",
      "created": 1649880629781,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007489",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "25bee425-6445-447b-a7f2-71023b9ef766",
      "created": 1649866373792,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008247",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "e593ff05-369b-403c-b7d4-cfe16092b716",
      "created": 1649851829204,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008079",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "f5c95cac-9c73-4c88-b4ec-a73cd9a863b1",
      "created": 1649837517215,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007878",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "77ee1648-62a3-42b4-98d5-850e59b697b8",
      "created": 1649822914893,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007953",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "80f0e9a4-556d-4737-b6a0-629b95166eff",
      "created": 1649808606043,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007663",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "19cfd5c3-d1cf-4301-8446-67902ad6e237",
      "created": 1649794299475,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008070",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "be19451a-e9ca-4dd5-b8ee-a1c1b02261b7",
      "created": 1649779584378,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006876",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "d9daa237-e069-4cb6-8cba-9e0b86ab0310",
      "created": 1649765367642,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008140",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "45cb2abe-c5b6-497c-89da-19b2cbebcb9b",
      "created": 1649750620861,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008141",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "e390f0c2-9fc8-47e7-b438-89d7accec16a",
      "created": 1649736444460,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008159",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "121fc7cc-d1ba-450e-8d6e-1fb324162211",
      "created": 1649721973487,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008078",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "98cb3496-1f34-40aa-824d-1b1a3fbbc233",
      "created": 1649707531234,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007978",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "23458de2-be2d-4a86-ba3d-10f24c36013c",
      "created": 1649693187099,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007901",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "b1b63abb-d324-48e1-868a-dd5398bd5334",
      "created": 1649678910576,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007659",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "ede5fd8b-f290-4975-8871-be7e39d2741d",
      "created": 1649664450407,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007725",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "4b45ad7d-9d09-4af6-926d-17cfd704b1f2",
      "created": 1649650043437,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007991",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "3b3d6ddc-ef82-488c-a2e0-976cd4b9c69b",
      "created": 1649635662101,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008039",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "7c16ef14-6c37-4405-b54b-d2c8f8bde7ac",
      "created": 1649621145852,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008341",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "d9932d5a-5419-4062-a6d9-29c35fbc5ba2",
      "created": 1649606731067,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008324",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "fc6af9a4-8ea9-41c4-9b47-243e81566eca",
      "created": 1649592508855,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008155",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "5faedc30-d652-4077-afd6-a5c4f119dfb5",
      "created": 1649578031416,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008108",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "a7f19ffb-9290-4f50-bdb3-6ca0dbe2580a",
      "created": 1649563686449,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008019",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "35a23a8a-6bec-4a73-9500-dbfd2c720c00",
      "created": 1649549242845,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008115",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "596ad269-d801-462a-b4c9-0de75cf63d05",
      "created": 1649534798394,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007829",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "82cbad5f-9965-46fd-8ba7-8c9423be3685",
      "created": 1649520499219,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007603",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "565da7b4-60a1-42c4-83ea-d798b61ac601",
      "created": 1649506090431,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007434",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "e8ffc1a1-b822-473e-b61e-e34679970b66",
      "created": 1649491346935,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005333",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000107
    },
    {
      "id": "7d1eb81b-c0fe-4da1-83a5-3721ba0b9e93",
      "created": 1649477185236,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007971",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "20ea1d7e-944e-4e73-8c44-aca61d9605e0",
      "created": 1649462810642,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007701",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "de86dd52-74e6-4504-9138-e82dc1d06caf",
      "created": 1649448263305,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007250",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "13707b21-0f39-42f8-99d0-422138874a86",
      "created": 1649434014946,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007486",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "292fa84e-5b77-4ed6-8880-aeceff1d491f",
      "created": 1649419645567,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007320",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "9a8e3e53-0f94-4250-9945-0d5039a3370f",
      "created": 1649405338169,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007070",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "a1df1c0f-ce1e-403d-8d87-1de2bbd87253",
      "created": 1649390747321,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007187",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "a977de50-51c0-424d-b10a-9924fdb99ead",
      "created": 1649376318987,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007546",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "5ad8589f-9e7c-4edf-a78a-ef4ac9d899f3",
      "created": 1649362039985,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007328",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "58cf1f5c-2594-4969-bae9-51e81de05e07",
      "created": 1649347599415,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007414",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "98ee583f-853a-4bab-b0d6-a1af45c06954",
      "created": 1649333260858,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007163",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "520ed26b-a963-4c88-9eb7-36aa7afa35fd",
      "created": 1649318823743,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007388",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "fd68a516-9890-4ae2-a02b-d652958c7796",
      "created": 1649304473129,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007757",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "50565773-a5a9-44a7-8c9b-8e0ed1f1caa8",
      "created": 1649290033989,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007156",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "da64f11d-958a-45e3-b341-dfe0acd633b5",
      "created": 1649275559092,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007882",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "7f469647-6612-4103-82c4-f95ddfe6a9f1",
      "created": 1649261211733,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007510",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "a3ea98a2-8629-4528-8107-16af45bcf752",
      "created": 1649246869785,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007428",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "09c5d74b-546f-4ccb-8bce-837fdeb161f5",
      "created": 1649232381379,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007431",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "43535381-f43e-4c37-9f5c-3a52c665141c",
      "created": 1649217995808,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007537",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "f97559b9-4b1c-483d-8f1f-62b2f2581327",
      "created": 1649203413017,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007115",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "177a2ba2-3ac7-476a-98e2-289e3fdba6bf",
      "created": 1649189152996,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008187",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "1b4f5df3-9db5-4ad4-afc9-6466d8678030",
      "created": 1649174762191,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007504",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "2157b3f5-5252-4fd0-93a4-51eb432db0ea",
      "created": 1649160496897,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007755",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "d1ecfcd9-8de5-4eed-8070-bd38fd899c24",
      "created": 1649146043505,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007604",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "bd91729d-2144-40c9-bd5d-dc0b76659dcf",
      "created": 1649131444968,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007333",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "ef7af6d3-4cca-40fb-ab7c-48cc2bc8d3c5",
      "created": 1649117191050,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007549",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "4108007c-19e9-4ef2-8ccb-44a5a2ea9b97",
      "created": 1649102743391,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007565",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "c417805f-040d-4ef9-892c-4547d10e152d",
      "created": 1649088351174,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007754",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "3c922f54-8474-4e00-b733-17843d207ffa",
      "created": 1649074015926,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007773",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "26b85471-0faa-4cfa-9f98-eb10870a0efb",
      "created": 1649059565160,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007740",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "1654350c-8ea1-499e-9f65-7bdd2cb93fc1",
      "created": 1649045232165,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007342",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "beacf236-d29e-447d-bf76-1781319e184b",
      "created": 1649030600754,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007640",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "377147b8-9dea-4397-b205-7ec6c75ac368",
      "created": 1649016348156,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007942",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "a4485d8d-a7c3-43f7-9bdd-1f60d9c85ab8",
      "created": 1649001857387,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007841",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "4da40ec1-c2ac-4969-9acc-08df718ff289",
      "created": 1648987567776,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007246",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "73dc0946-b6f5-4cb9-82ca-736758341ca4",
      "created": 1648973342244,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007335",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "4e06fca9-bbeb-45f8-bc17-3960b9158adf",
      "created": 1648958644750,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007981",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "a592234c-40a0-49e6-9d1a-9cdd3655b694",
      "created": 1648944227002,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007665",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "f5d3cf55-0450-4d17-bcdf-a80d421d1ccc",
      "created": 1648929864123,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007800",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "a7ac35e3-1f48-4581-8e5f-ff9179bd540f",
      "created": 1648915526204,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007819",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "92545d82-2ca4-4536-b941-3694e19f6eeb",
      "created": 1648901120528,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007610",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "f871b770-a1ab-4ad1-92ad-125bd0e9cd23",
      "created": 1648886697213,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007527",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "1eb0f2e8-88f6-46a0-9e8f-1f5102e9fff3",
      "created": 1648872272720,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007363",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "ab40082e-8116-4800-835e-34fdd5ce72cc",
      "created": 1648857833704,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007217",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "a0cdf569-c6cd-4aed-937f-a68fdeb257e6",
      "created": 1648843587564,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006828",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "5429ef57-f6e3-4037-bf04-92ddc0e9ff5b",
      "created": 1648829166694,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006685",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "124ac7fd-20ef-4a96-a625-4f777631d178",
      "created": 1648814682743,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006810",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "f4e53a34-004b-4277-aae2-0608f18c5969",
      "created": 1648800309086,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007220",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "f2a0ec35-cef8-49ad-a0ef-67e1eea8c197",
      "created": 1648785837032,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007522",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "e8fb2834-13cd-4cec-bdc7-2565d78d95be",
      "created": 1648771468283,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007381",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "a88a79bb-7bb9-450b-8958-1970706c4d4d",
      "created": 1648757054409,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007196",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "62d9d638-0253-4bc5-9c78-83d5b5e79ddf",
      "created": 1648742768199,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008245",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "940f0528-cc34-43d3-9416-b245e76afad6",
      "created": 1648728353787,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007825",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "40d4e5d9-3174-4409-b7c4-b1fb15c349b4",
      "created": 1648713938994,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008190",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "80ac9bb9-fe34-46af-b996-ceb7c8257ae5",
      "created": 1648699459456,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007978",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "67ffaf60-216f-44cd-ad79-df9fe0f9c7c1",
      "created": 1648685114501,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008072",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "20a1f681-ab28-41b1-8f4e-3ad02db0de22",
      "created": 1648670786625,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008413",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "b34b0724-bfdf-487f-9e5f-0794efcbf96e",
      "created": 1648656430455,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007795",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "6f3668a5-e8aa-4950-bdb2-ee404e105667",
      "created": 1648642074144,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007907",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "666ccce3-d373-4439-9de9-dec78005f1a6",
      "created": 1648627521064,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007744",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "fbf9fb7b-047d-45d6-b3d4-0046a5e54811",
      "created": 1648613080552,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007629",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "e2d91b19-b26c-424f-96f7-d8ba97b768a3",
      "created": 1648598629212,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007805",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "2f4e8b33-adf8-45f1-a79a-e078e69024bf",
      "created": 1648584344788,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008180",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "6c0b78b0-a3ba-4488-b580-97b3eff9d67f",
      "created": 1648569935224,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008429",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "8572cffc-b692-4cba-992a-b1acf46e067c",
      "created": 1648555753866,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008014",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "05f81db8-e20b-42da-9f2d-6e63c8bd7d4d",
      "created": 1648541404444,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007846",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "5cc3aaa5-ad48-4b4c-a4b8-3d0a8e5b2c92",
      "created": 1648526745555,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007816",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "0ee5a9fd-204a-48af-920f-ac14d7f7f849",
      "created": 1648512272516,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008006",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "352a76ab-cc2c-47fe-a7bd-d73945ea8a5b",
      "created": 1648498142992,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010110",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "c3d0c1c3-2c01-48c7-a51f-b535715535cd",
      "created": 1648483675306,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007766",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "0dbb1d00-66e7-4fc9-9a82-65cbe1a9cba8",
      "created": 1648469519297,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007339",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "8cc94942-f3ac-4304-a2f1-2cfb9420b4d0",
      "created": 1648455012712,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007206",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "a73e2396-37cf-4392-b202-d522bcc9966e",
      "created": 1648440325134,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007562",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "def04f57-5a4f-46a3-b4cc-afff2812eb64",
      "created": 1648425850027,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006831",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "18e4e913-a762-4f2c-9cf6-4a93ce1c4a4d",
      "created": 1648411806727,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005111",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000102
    },
    {
      "id": "5ccad49d-48a5-491b-a7d8-f6f9e7b2a58a",
      "created": 1648397316296,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005511",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000011
    },
    {
      "id": "331fbdea-002e-4050-b773-823478d1637a",
      "created": 1648382912226,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005613",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000112
    },
    {
      "id": "6d5d7188-3145-4518-b1b5-ec4b92c97077",
      "created": 1648368520964,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005526",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000111
    },
    {
      "id": "a8a6af93-47b9-4025-9e5c-93752239cbf4",
      "created": 1648354189393,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006164",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000123
    },
    {
      "id": "cdeb7444-21ee-488c-81f3-9ff7fc84981d",
      "created": 1648339520678,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005434",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000109
    },
    {
      "id": "077fc15e-e6a5-4c4c-b179-147a7ff9b26c",
      "created": 1648325187508,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005397",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "a3a0d4e5-fe02-40bb-9e35-39c765d95ab5",
      "created": 1648310741882,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005479",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000011
    },
    {
      "id": "b0c1bded-b29f-4b12-b08b-81291d7b5d2d",
      "created": 1648296402829,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005236",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000105
    },
    {
      "id": "97199dfd-8fa4-4f02-94c0-51aeca293151",
      "created": 1648282063977,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005102",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000102
    },
    {
      "id": "e2bec225-3f28-43a5-8ec2-c3ca7edbadf4",
      "created": 1648267604420,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005180",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000104
    },
    {
      "id": "141bdff1-e931-4d44-adcd-1a3ca1ff5142",
      "created": 1648253283301,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005543",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000111
    },
    {
      "id": "b916b5b7-c610-4ec8-aa39-a885066cc290",
      "created": 1648238754812,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005276",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "82b8f8f4-57cc-4bc6-856a-97448c7252f1",
      "created": 1648224539376,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005376",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "b7d6a490-62a3-4eff-8a57-cde25e97f9d6",
      "created": 1648210219576,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005376",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "2063bac8-3c77-4c06-9500-0ac21a48eb6f",
      "created": 1648195751155,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005356",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000107
    },
    {
      "id": "d8b21c23-7455-4efb-9e2d-49eeb496277e",
      "created": 1648181230072,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005294",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "fbecc615-2ed9-41b1-a375-c1c4ccff527d",
      "created": 1648166777466,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005467",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000109
    },
    {
      "id": "68c0d007-e20e-4977-a1db-ee1b0756967f",
      "created": 1648152434802,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005491",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000011
    },
    {
      "id": "52d373a5-0c26-4525-8b2c-eac9640c53a4",
      "created": 1648138117321,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005485",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000011
    },
    {
      "id": "042f167f-e0e2-492e-a5ca-bcf65984149f",
      "created": 1648123637564,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005345",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000107
    },
    {
      "id": "715f8def-e1cb-47b7-b267-90b760c6c7a3",
      "created": 1648109278243,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005593",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000112
    },
    {
      "id": "51c01d42-c1e9-48bb-ac46-506cc78c1ca7",
      "created": 1648094789581,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005518",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000011
    },
    {
      "id": "64437bce-23f7-448c-bdbf-da0803792324",
      "created": 1648080377984,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005348",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000107
    },
    {
      "id": "8b1a260f-3532-44d0-a7da-f3aabf2bba09",
      "created": 1648065970003,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005323",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "5e043ad6-75ad-461b-8886-33662ef1ffa0",
      "created": 1648051759889,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005314",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "cbd8a8a1-5ea7-4835-b47b-cc4bbc441661",
      "created": 1648037471547,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005195",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000104
    },
    {
      "id": "f848a00f-fb66-4962-adca-42b36600f8e9",
      "created": 1648022826660,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005139",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000103
    },
    {
      "id": "e29839da-a979-4e6d-a61d-872de65438b1",
      "created": 1648008327798,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005202",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000104
    },
    {
      "id": "cd298f07-7e23-4836-bfff-861c2579b7ca",
      "created": 1647993953673,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005530",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000111
    },
    {
      "id": "391deded-bb17-4f1e-944a-72bdb27f4ce4",
      "created": 1647979590224,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005318",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "1ed01876-5b0b-4bb1-9b86-469cb27ee01a",
      "created": 1647965382854,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005103",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000102
    },
    {
      "id": "0b558a1e-acd7-4b58-8403-81dac38b3986",
      "created": 1647950901273,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005381",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "e7df88c7-fac6-4b51-ab9a-aab0b6808f22",
      "created": 1647936573280,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005397",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "74a19bf7-eac8-4239-9e0d-9506bffcf76c",
      "created": 1647921860755,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005652",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000113
    },
    {
      "id": "385bf4f7-1a82-49d9-ab3a-3071e7030c88",
      "created": 1647907531440,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005664",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000113
    },
    {
      "id": "c265da4f-2f83-4798-aa0c-d776e2143937",
      "created": 1647893114328,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005301",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "5ac054f2-c6ed-4e51-bfc6-78b40da5a8cd",
      "created": 1647878731505,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006373",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000127
    },
    {
      "id": "e313e37d-01c8-4a3d-8697-0ff6e9b685a6",
      "created": 1647864279583,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007809",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "7e032427-4ae3-44d0-b093-76a7ee515da8",
      "created": 1647849993386,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007746",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "d7ac4de1-ba69-48a8-825a-d33c472abea1",
      "created": 1647835471545,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007501",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "8bc59014-afb8-43b4-a2d5-658aab3941ee",
      "created": 1647821174929,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007569",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "61b10e7f-213b-4b64-b8a4-df435086e2ca",
      "created": 1647806640931,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008015",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "2692a95c-1f4c-419a-a4af-d7db8dcd2216",
      "created": 1647792415146,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008395",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "9ee6f0ab-1887-4101-ac39-f4c4280b2015",
      "created": 1647778014325,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008175",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "7783fac4-1975-4bf4-84c3-d002d20a6d10",
      "created": 1647763459708,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008199",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "37bde39a-65a9-42bb-b873-e79495c55bc2",
      "created": 1647749152334,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007899",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "55a81e39-1c19-43fd-ae32-d87fe7aa6fb7",
      "created": 1647734638239,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007968",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "11346c67-51a3-44fa-ac77-86c4d21a14b5",
      "created": 1647720283260,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008188",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "22f09d38-c773-4143-ab42-a98924924169",
      "created": 1647705939097,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008089",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "fd1ad4d1-a2e8-4bc2-a6f7-09760e972aed",
      "created": 1647691547025,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007909",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "dd78da47-fe69-4a0b-969e-b6b8139ce03b",
      "created": 1647677382988,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007817",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "245a107e-66e8-4e74-a508-ba544e62aca9",
      "created": 1647662724146,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008346",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "cc254b4f-6d98-490f-a947-55053b749e52",
      "created": 1647648220720,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008260",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "d769af7f-52f5-453a-b6a9-8218eed8b109",
      "created": 1647633966740,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008336",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "bc44cd9b-77ce-4201-b3b5-8d6215a484c5",
      "created": 1647619418341,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008342",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "fd3f83d5-21fe-487d-acb8-4cafb3326bfc",
      "created": 1647605079926,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008254",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "71f21715-cc38-4c98-ad52-56d9f913a53c",
      "created": 1647590691618,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008173",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "abb6b304-56fe-4034-a648-f116b8e73cbe",
      "created": 1647576288911,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009472",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "e3ab14ba-fa8c-4751-b16d-34c61b97bb63",
      "created": 1647561844321,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008343",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "a5c250ec-7185-4916-b4ab-a61ac36baa19",
      "created": 1647547462131,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008379",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "37e4dcba-e3c5-4419-ad51-9f1a68608bde",
      "created": 1647533130190,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009591",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "7c2ff7a0-42b7-492c-a4b7-bb660ae0d577",
      "created": 1647518730233,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007677",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "704fd6fc-0b95-47bc-8e53-a76362c343f8",
      "created": 1647504439753,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007428",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "b695a807-d9b3-4f2f-95b4-15a547c5fa62",
      "created": 1647489850521,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007645",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "b88c2f55-64a5-41dc-97d5-8c990bda8aed",
      "created": 1647475476085,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007626",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "105fcfc1-424e-4ff6-9be0-e771e834a77e",
      "created": 1647461022059,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007185",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "b1720540-2b74-4815-9514-99331ad088f6",
      "created": 1647446795247,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007392",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "e2adc97d-3075-48ff-8a27-0eb3d43ad049",
      "created": 1647432199058,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007096",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "e2f7cbf8-e035-497f-86f4-c51082c2cb28",
      "created": 1647417874056,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007389",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "0e07eca6-1c07-4e6c-ae0a-c79a29b39f51",
      "created": 1647403438206,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007327",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "851f4122-c5dc-48c9-bdf4-ea092e47a66f",
      "created": 1647389174261,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007010",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "b27e06ed-8217-4484-972a-5f1ee78622d4",
      "created": 1647374612771,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006837",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "badc425f-1077-429b-b1c2-6f171d095c98",
      "created": 1647360305510,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006723",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "603ba050-840f-4fa8-a301-34a7c040fc32",
      "created": 1647345856800,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006894",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "632935d6-778f-460f-8618-1104f40b0ed4",
      "created": 1647331594356,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006793",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "b4d8aca5-9954-4941-bf49-72345270920e",
      "created": 1647316980500,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006487",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "38029500-cfe2-40dd-8720-45ca1020470a",
      "created": 1647302669838,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005042",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000101
    },
    {
      "id": "65048d00-5fa4-49d2-877f-2a200a6b5bb4",
      "created": 1647288406117,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004249",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.5e-7
    },
    {
      "id": "fdc5cd9f-45e4-4c55-9c8b-2d3e89aa1634",
      "created": 1647273863593,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006818",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "b2476bc9-706a-40c8-8dac-e95c110c4054",
      "created": 1647259424013,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007144",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "8a339419-a78f-4613-a737-842331749deb",
      "created": 1647245048994,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007152",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "8b4b003d-77f9-4921-a6ac-0b23b7ce4768",
      "created": 1647230633438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007015",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "67fb542b-2884-49e6-aacb-d795b54d43ef",
      "created": 1647216244522,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007101",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "52f3cd1f-67c8-410f-93a3-ca737e7e6320",
      "created": 1647201774816,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007505",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "f02b4d43-b83c-4a26-b3c2-f2118e3825d9",
      "created": 1647187493603,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007034",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "df30b6cc-e6c3-471e-8d9e-e9d15531150c",
      "created": 1647173034235,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006965",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "19299be9-d8d7-47fd-b272-69334f37b6c7",
      "created": 1647158676145,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006764",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "65880b87-331d-4575-aa7b-109f7eb4420e",
      "created": 1647144303215,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006608",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "ef3c9fd7-2589-43d1-89b1-d957e251432d",
      "created": 1647129847137,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006697",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "8bfbe41d-75ad-4880-bcca-ab91ecf99284",
      "created": 1647115462907,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006955",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "4b6a090a-ae99-4bec-a4c5-c86efa883777",
      "created": 1647100980329,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006585",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "bdf0c837-ef40-4dd0-ace0-f81a0642b146",
      "created": 1647086824584,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004313",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.6e-7
    },
    {
      "id": "898d2e02-70b7-49f7-b828-109af2bbdeb1",
      "created": 1647072278296,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005552",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000111
    },
    {
      "id": "9c4c9933-35ed-46b6-84ee-979886865560",
      "created": 1647057821213,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007001",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "fe8dc8f9-17b8-4a7c-b966-bbb4a670085b",
      "created": 1647043454181,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007412",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "edbe9671-202a-4f35-abfd-edbd987ced91",
      "created": 1647029047793,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006820",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "9480ba50-3eff-4b4c-837f-eb10a544ce3e",
      "created": 1647014559742,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006513",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "9520c388-1ff7-4528-96fc-53529d4bd150",
      "created": 1647000226619,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006722",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "1955d116-62f6-4ffc-b1bb-1a32a5b17c48",
      "created": 1646985849822,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006799",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "8d326ffa-0642-41e8-ba43-20a44749ec25",
      "created": 1646971476768,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007066",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "441204ea-7281-4891-85d1-fb348338e2c2",
      "created": 1646956974438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006859",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "ba75ba61-8211-460e-8a20-781a37c33b69",
      "created": 1646942615854,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007120",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "70586577-a54b-4715-a2b0-c839a8d121c2",
      "created": 1646928243900,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006512",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "11358574-6b3d-40e1-8724-eeb42f004ccf",
      "created": 1646913894298,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006590",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "48d94cde-e8b1-48b9-94a3-2f1a0c3055f1",
      "created": 1646899447484,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007514",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "fd52ba7f-ebb6-4fde-9e99-f7919a97debc",
      "created": 1646884972980,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007719",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "cefbea04-bacf-4789-9ed0-d75f0bab164e",
      "created": 1646870625442,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007942",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "17b6d2c8-2fcb-4128-ab1c-f9e6d3ed9cbd",
      "created": 1646856194493,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005416",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "7e74454e-f5b6-4a07-8fc8-a0cf1e989db8",
      "created": 1646841765771,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005877",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000118
    },
    {
      "id": "df0bdecb-72a2-4ff5-987b-da51122ba9b0",
      "created": 1646827393935,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007112",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "0ffd11a9-cade-458c-adca-337e442ec17b",
      "created": 1646813018974,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007193",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "08579e1b-9a6c-41a5-8f29-3e84f857c900",
      "created": 1646798575872,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007306",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "a2b1c745-75eb-4ee1-9990-6849f89e51df",
      "created": 1646784211792,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007361",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "97871924-428b-4fbb-8b5e-e4446a11e35e",
      "created": 1646769812831,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007898",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "f7c14eef-bda6-4dce-96d5-e9afd5b5d9db",
      "created": 1646755376405,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007981",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "c7305534-74af-4fd0-a264-b62f3e93222f",
      "created": 1646741075489,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007538",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "c241dd4c-1fc6-4ca6-8b76-1ec160100d1c",
      "created": 1646726648033,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007674",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "7b8ea666-dae1-4635-8338-51850fb69731",
      "created": 1646712192369,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008013",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "4ddd8a7c-0387-4ea0-8980-a7c9d781025b",
      "created": 1646697991666,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006950",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "7df9e2d4-50ee-4937-a48a-cd9428709a8e",
      "created": 1646683421396,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007094",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "0b8a86ce-0254-4119-85df-f34578e78e2e",
      "created": 1646669044669,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008107",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "af2a63b6-a6c2-4347-8c48-e7d851c62407",
      "created": 1646654686172,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007399",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "abcdd4c8-5517-4fb1-a14d-ed296e33183a",
      "created": 1646640210634,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007673",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "07b3e492-4e16-4009-b0a5-83d88e58763b",
      "created": 1646625864358,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007605",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "7ea1954c-7d99-492a-933e-aef00ea93561",
      "created": 1646611456656,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007611",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "5495a781-3ae1-45a8-b133-496e3d7a139c",
      "created": 1646597006580,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007741",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "f287550e-e882-45a6-8ec9-5f7374690c48",
      "created": 1646582667242,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007439",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "5b0dc020-2b78-49ca-a2c1-934e2e05f1b6",
      "created": 1646568264526,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007498",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "481b6df5-b1cf-45f0-85dc-b2bcd78aaea2",
      "created": 1646553899237,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007304",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "ea4a011b-9c96-4117-9ef6-b147f3c792c8",
      "created": 1646539438952,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007612",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "0e8a4bc0-25a6-4f07-9191-817f72d74a86",
      "created": 1646525096110,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007668",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "83d10c1b-d304-49cf-b2e0-9abcd2137881",
      "created": 1646510589616,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006914",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "f1307246-932d-4cd9-a20f-7e16a47b706b",
      "created": 1646496213682,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007537",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "0556a394-a782-4082-8972-4c52d6c3caee",
      "created": 1646481981092,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007185",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "1fa7870e-4fe3-4a0e-99da-0915eb42b051",
      "created": 1646467384680,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006939",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "f2c5526a-73d5-4773-95ba-b94cf94ccc1b",
      "created": 1646452967361,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006804",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "5c4f7311-a7e9-455c-a6f5-25e29d4aae8d",
      "created": 1646438703161,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006845",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "964a5f73-e7a7-45a8-9cc6-253eca169fab",
      "created": 1646424176958,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006741",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "a52971c5-2043-49e7-b790-766a60ce0bf0",
      "created": 1646409751729,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006987",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "beb22344-3dfb-4f27-b405-5892bf9aa7e4",
      "created": 1646395408224,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007043",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "ad46224b-9f19-44bf-bbd2-ab5dd3badfad",
      "created": 1646380950516,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007087",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "0d23ba22-fe56-4f71-81ae-6cc71c15ebb6",
      "created": 1646366650416,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007202",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "58a515ef-ffcb-488b-bc9a-edb8233f3de7",
      "created": 1646352194696,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007117",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "6fc09915-e602-43e7-9ef0-d13a7cdf69c1",
      "created": 1646337816645,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007192",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "6fee2371-51e5-4d68-a5a1-fcc487fad2c1",
      "created": 1646323487035,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007113",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "cdb544d4-2def-4a67-a421-d04ba3ee0a41",
      "created": 1646309064340,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006687",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "ce9c9829-fcc9-4ce5-9086-c662866a3210",
      "created": 1646294642182,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007026",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "c4b74ac9-0318-43e6-88ae-f91668c39ee3",
      "created": 1646280319055,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007342",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "1c18d9a0-7b09-4e0c-9743-920ec96189cb",
      "created": 1646266005442,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006242",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000125
    },
    {
      "id": "c76e58bf-e41c-4c1e-b193-8cf0b5fa1a82",
      "created": 1646251562317,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007011",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "fd02b105-b9a0-4ff2-9e22-fe3799165093",
      "created": 1646237179682,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006918",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "3511e743-de0b-4343-9dc2-78cacfa5334c",
      "created": 1646222730053,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006942",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "7734ead9-ef57-44eb-a930-970f44fb3d66",
      "created": 1646208282530,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006533",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000131
    },
    {
      "id": "bef79eba-5841-442d-98c4-6f2a626f3e1e",
      "created": 1646193952650,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005502",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000011
    },
    {
      "id": "66edcb30-a835-481f-8a75-41f48738e3dd",
      "created": 1646179659635,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005076",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000102
    },
    {
      "id": "42a49d39-590a-4e51-ac10-e1561da7649d",
      "created": 1646165073070,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005299",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "19f02e88-d70e-44f9-9fe3-9c042f5f03bc",
      "created": 1646150950284,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005878",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000118
    },
    {
      "id": "d3e3bd64-7238-4818-8b72-122f77787f87",
      "created": 1646136223331,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007060",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "7d21bf67-0e91-47bd-b8ac-5caa71bc24de",
      "created": 1646121804645,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007076",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "d460e977-a97a-4272-af29-fed6c86d5a3b",
      "created": 1646107498016,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006992",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "c8022ded-b36a-45cd-a10a-90d84a4251b9",
      "created": 1646093140261,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007308",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "63fdd62a-3e7d-48bd-826b-b36a1de670f9",
      "created": 1646078645399,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007359",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "0aba5a49-678c-4ec6-8b4b-40e647c3d57d",
      "created": 1646064267751,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007161",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "27c6347c-3d6a-4705-9183-d58b511b62a4",
      "created": 1646049899757,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007204",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "dab71004-7595-40fc-ae2d-1891ded2ae49",
      "created": 1646035484692,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007226",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "a6db6c85-f51f-4fff-8502-fff8c4ef26ca",
      "created": 1646021072307,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "3311f7a4-dd50-444f-b142-400b71c271d8",
      "created": 1646006591114,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006303",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000126
    },
    {
      "id": "2355012c-9298-4465-97d6-785b10e3293a",
      "created": 1645992192585,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006714",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "036c058e-693a-4137-87ba-d9308cbcda10",
      "created": 1645977872439,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007263",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "2617ef4a-9a22-4730-934a-ca886509afe3",
      "created": 1645963584872,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007251",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "9bad58c2-a1d2-4cec-810d-e17651e5c4f6",
      "created": 1645949128013,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007063",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "8db10e12-8f33-41fe-af2b-bd1d04a5b210",
      "created": 1645934678101,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007169",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "ad3ad9d4-c85f-4024-b070-530351bda828",
      "created": 1645920167280,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007089",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "8b916102-4996-43d0-91d5-caac1e6f0ae0",
      "created": 1645905861296,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007246",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "a65920ca-588e-4191-a299-f3bb2c42ab48",
      "created": 1645891551647,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007872",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "b5ab65a9-73e2-4310-a577-d686bd51e904",
      "created": 1645876997438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007633",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "0df2eb18-3218-44b9-8f2b-7dffccfc00b3",
      "created": 1645862803214,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007598",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "a5fdc7f9-8daa-4d42-972f-6ac97bce9291",
      "created": 1645848171770,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007844",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "ddbc66c9-d77d-4281-84b8-7253a3e0ce5c",
      "created": 1645833872911,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007586",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "dcbcf9cf-587a-4550-adaf-e483023bb2b9",
      "created": 1645819366277,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007495",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "95a3bdd7-0f53-431c-acdf-239fdab634f0",
      "created": 1645805270925,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007378",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "6c6e7e2e-a59a-4729-98a1-d4f9259752cd",
      "created": 1645790792327,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007154",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "c4889c48-a0cb-4e26-809c-9eafbcf06a4b",
      "created": 1645776249081,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007023",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "f8f9aa67-49cc-4a9e-a584-213d70251c11",
      "created": 1645761878228,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006861",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "c4aef4bd-1eef-4733-98dc-426822ccd455",
      "created": 1645747460342,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007228",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "cf4b8435-c861-40eb-a218-1501510a6206",
      "created": 1645733063368,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007219",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "db82e96f-01df-46f8-80a0-c03095358aa0",
      "created": 1645718677925,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007316",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "48103169-a7b0-47b8-85f9-8e7e6cdbd29a",
      "created": 1645704285205,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007298",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "643fb3fa-7aae-453c-a43d-fe9ce20219db",
      "created": 1645689797704,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007493",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "4a49cab8-27b6-421d-93f6-109c7e8a31b8",
      "created": 1645675503893,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007000",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "1f61794a-f872-475c-9eaa-f90da313cdd6",
      "created": 1645661059832,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007312",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "a3b5bd2e-20e5-43dd-8ce0-b1ffc995e9d4",
      "created": 1645646812398,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007809",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "5c641c51-2b3f-461a-a731-9cbd364b8425",
      "created": 1645632298522,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007152",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "2ae067c8-79b4-40c1-a3da-a45b4dbc0168",
      "created": 1645617863728,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007413",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "48c2d725-33c7-4afa-8519-fc6f9e329c4d",
      "created": 1645603448267,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007129",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "218bb182-6a9c-4513-b80c-aba2a1453b6d",
      "created": 1645588994102,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007469",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "74200d7f-a912-421c-a79c-1837f9768163",
      "created": 1645574666231,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007336",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "f85df7a8-a0f5-4375-a49b-3a4f1e71d484",
      "created": 1645560281940,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007488",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "97681bed-9478-4c7b-8f22-d3bdedceffbb",
      "created": 1645546037287,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007239",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "a4facd47-6b9e-4e7b-8f7f-08e2b6af7191",
      "created": 1645531438906,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006177",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000124
    },
    {
      "id": "b5c4c438-92e8-4f37-9097-bf606f7985bc",
      "created": 1645517089916,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007095",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "705e527c-2d37-4df8-80bd-af7e9e450378",
      "created": 1645502672727,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007188",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "0e3e2b71-97f7-4a55-9bd5-5d4291efe9dc",
      "created": 1645488291135,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007315",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "11f502cf-5b4d-4dcd-b37b-7dd0994cf2e0",
      "created": 1645473915557,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007342",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "5e3ca3a7-8c55-493f-9805-8c30e5dee728",
      "created": 1645459530297,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007229",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "8f34ef8d-6515-4f00-97df-b8fbac764104",
      "created": 1645445027873,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007349",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "3072b989-0cc4-4f0d-82b0-a42ea0c6d49f",
      "created": 1645430578287,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007056",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "87b10a0f-0a21-44f8-887d-6e42c8f0578f",
      "created": 1645416425582,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "3b4986ac-3ce6-4659-a762-02eb86b8ce3f",
      "created": 1645401869169,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007376",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "4391a515-7927-4621-8cd3-cb39cc4b02f3",
      "created": 1645387476872,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007356",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "2063638c-b5a1-4cec-94a4-1d8a1fa42d7b",
      "created": 1645373265780,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008303",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "51f45878-de40-46b4-8790-9d7e6d310b2d",
      "created": 1645358729005,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007331",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "392c52c8-a7ff-4e78-81f8-e546a7828808",
      "created": 1645344344548,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007091",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "db2ed970-e2ec-4b89-a506-4648a528310f",
      "created": 1645329812031,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007633",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "4bf54bd7-c03f-4433-8208-67e05801e916",
      "created": 1645315294240,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007632",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "86307210-534a-485e-942b-2699af972df2",
      "created": 1645300960013,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007605",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "dacbaaca-4fca-4fa1-884a-637c866755c6",
      "created": 1645286475563,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007179",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "d183cbed-e782-4c73-bd0d-e5a18287a51b",
      "created": 1645272056520,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006884",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "d2b36f5a-bfd9-49b7-abe8-021db64cd18e",
      "created": 1645257811914,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007233",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "da4b06c6-0f04-4a5b-aab5-087b0c4effb5",
      "created": 1645243404854,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007215",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "567bb92d-2d1c-4db0-a52b-686f1dbb16fe",
      "created": 1645228858876,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007283",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "ba1c4fe2-95ae-4cd8-9a62-d593b26918b9",
      "created": 1645214433373,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007381",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "c0a3da08-bd4f-4d80-bca9-3fcf9964e6ef",
      "created": 1645200112229,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007323",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "35f54c90-f7e2-44f6-897b-bf33a1671ab6",
      "created": 1645185870895,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007579",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "c9140742-56b6-4a96-8536-aeb287852648",
      "created": 1645171286374,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007439",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "a4423d22-ec10-4253-a690-c234ba684e78",
      "created": 1645157057047,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007451",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "cc5a06c9-a679-4643-8ae7-0f67034cebde",
      "created": 1645142436693,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007258",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "ad86890f-7ee3-4c4a-bd19-35e8d9172397",
      "created": 1645128119119,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007758",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "65eb8625-ab53-4d41-8e08-c6a6f764503b",
      "created": 1645113644113,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007718",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "b1ea0a97-9f1a-4a4e-8bc1-02db38ab6978",
      "created": 1645099272736,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007217",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "4cd79602-eea2-44f8-8fd2-f82f5dc67753",
      "created": 1645085155579,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007320",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "6f89146e-fabe-4e7b-aa13-bcabf4dd2183",
      "created": 1645070555596,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007493",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "2da37efd-f64b-4578-a4b7-37ff37a773fa",
      "created": 1645056153021,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007392",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "5b74f163-74ee-4250-af49-dbdec228371e",
      "created": 1645041923228,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007484",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "7d31a69a-5812-42b8-9878-08a0cd490093",
      "created": 1645027240024,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008198",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "37df6ae0-bc4e-4625-8b90-a29d4c38f876",
      "created": 1645012962481,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007407",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "18961764-683f-487b-a94f-1901a65ef5f7",
      "created": 1644998531140,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006971",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "046281c2-6dcd-45ec-81e0-130378d828d1",
      "created": 1644984075185,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007327",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "f3dc5d97-e3c1-4fef-b6af-37a09880820e",
      "created": 1644969632005,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007014",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "ae50ab82-3b2c-4bdd-b254-1985ee38e8d9",
      "created": 1644955427694,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006876",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "3cc93873-0fd9-4ce3-ad7b-9d7837956cc8",
      "created": 1644941058233,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007025",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "465edcbd-3cec-46f0-9c68-92af4aa90b47",
      "created": 1644926471820,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007221",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "98b3d6ca-fcf3-4503-85ec-cea2ea9ea1e7",
      "created": 1644912151561,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006952",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "2c668483-9862-4700-9b1c-ba2223a8c0e7",
      "created": 1644898192727,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008319",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "fbda6dc3-0bd4-49f7-8277-eb93c18782e9",
      "created": 1644883294431,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007022",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "6b323a1d-0d45-4016-8fc6-5aa2b48d2eac",
      "created": 1644869267962,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007252",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "a8558733-5e2b-40d6-9d6e-b8f26f7fb595",
      "created": 1644854833962,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007039",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "96e56f80-2e12-4917-b351-08000aa575cb",
      "created": 1644840439477,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006924",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "b1a123cb-915d-4fc3-80eb-2822ace24d52",
      "created": 1644826014101,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007123",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "c9cd14b8-c53c-4a51-99fb-9f4d3a39d5c2",
      "created": 1644811672726,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "9c4ce567-ce91-48ca-bb44-5af0fbdae768",
      "created": 1644797197983,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006682",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "db6cb4da-e74d-403a-a75b-01eaaf56dfed",
      "created": 1644782708230,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006990",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "86a93125-71f2-49ce-89af-eadb92827d5e",
      "created": 1644768210162,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007166",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "2e84beed-a845-466d-94ab-200991cf2854",
      "created": 1644753817579,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007053",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "ec3fd0bd-c576-4ecb-ab88-58ecd522ec75",
      "created": 1644739562913,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007202",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "778f2f2e-c6c0-48cb-9bd4-453a537672c6",
      "created": 1644725043855,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007158",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "8eb84883-0eb5-4dd9-af08-1fdb67a6822f",
      "created": 1644710479745,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007239",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "6710f364-7c19-41f0-9637-e245b898a054",
      "created": 1644696232030,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007285",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "e4ae694c-ab35-4ce9-acdd-c97c4f9bb00e",
      "created": 1644681938247,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007345",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "6610c63c-f035-4655-b2d2-430baef1db11",
      "created": 1644667248066,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007478",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "f36576b5-9dd1-44b0-b127-3982f26da381",
      "created": 1644653110344,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007436",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "2828d52c-0724-4b62-aa9a-48ab95152df7",
      "created": 1644638407475,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007145",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "38b8ccbb-6231-4588-9dfc-8e4d3165cd0b",
      "created": 1644624309227,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007449",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "cd207e6b-932b-48a0-aa2e-3e40a8ac4a1d",
      "created": 1644609995116,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007524",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "10b8c611-b5dd-4b56-b519-494c3f59c069",
      "created": 1644595576101,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007628",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "4735aa4c-9dbf-40ac-8050-2d822ef1d1cf",
      "created": 1644581163658,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007830",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "e9c78a04-93f4-42a3-a53b-6119b56f9e57",
      "created": 1644566697599,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007694",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "39975a21-c0db-422f-afc2-583c0befd0e0",
      "created": 1644552250665,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007749",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "fb2ad173-9c60-43b8-aa02-2871c3cf33e3",
      "created": 1644537943728,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007335",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "210e86e7-cd6f-4567-ac19-42e311cbb39e",
      "created": 1644523483352,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007498",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "944c163d-44a7-4556-a712-53b3be9b3b05",
      "created": 1644509156036,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007182",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "e7f0a640-9091-4118-9e74-c1047576de9c",
      "created": 1644494684602,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007442",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "73ea7544-fa43-494a-8c31-d9d6a3a6acd0",
      "created": 1644480270891,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007356",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "eb783110-748c-4df9-848f-279116ceb05e",
      "created": 1644465876881,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007668",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "70c82244-8eed-4ff5-b5f6-290557493be2",
      "created": 1644451532424,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007002",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "17f61617-cb76-4c4a-81b3-348863c90ea7",
      "created": 1644437199438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007896",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "b7431bec-b43c-4736-9afc-6d7a252a8931",
      "created": 1644422732964,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006853",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "fa731a18-3f90-44d9-ab5c-7e292aa9e639",
      "created": 1644410086141,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007115",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "be6ae904-d947-40ef-a68e-453e834fc159",
      "created": 1644394009254,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007333",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "eb136f45-bc29-4b16-a326-3de329f5a160",
      "created": 1644379530637,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007317",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "45c5f978-1e1f-4cfc-9da8-e823eb3c2996",
      "created": 1644365019841,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007360",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "3bdc5977-9bf5-4b61-b5c2-fe43eaab7b9f",
      "created": 1644350788508,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007489",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "1b53bf6d-2f07-418f-af87-effc7846c4cc",
      "created": 1644336367175,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007203",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "7d114f46-486b-4fc8-add9-b1b6d97d9c7d",
      "created": 1644321936650,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005993",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000012
    },
    {
      "id": "d381ab55-f67f-4d90-ae0c-4ae7e76f8ef5",
      "created": 1644307545926,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000012
    },
    {
      "id": "091b73f7-3cfa-422c-aedf-dd62c6d96ea6",
      "created": 1644293026347,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006117",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000122
    },
    {
      "id": "1b330d30-ed68-4f09-bc8b-17336f74fbf0",
      "created": 1644278724576,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006578",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "b10acd4b-2dd2-49d0-ac4f-08a119ebc6fa",
      "created": 1644264293523,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006881",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "7992e1a3-56c4-45a5-8d5c-a21fa34392f9",
      "created": 1644249945254,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007761",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "5b506bc0-c0a0-4fb9-af7f-4d91614f3249",
      "created": 1644235444340,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007666",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "6d775494-bf32-42d6-bc98-ea89422287cd",
      "created": 1644221266034,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007481",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "4949461e-84f9-4915-830a-7b0cad699f80",
      "created": 1644206620960,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007353",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "72d384af-90f8-4140-bc1d-d5a8a1b82355",
      "created": 1644192363602,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006162",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000123
    },
    {
      "id": "18db4cae-6918-4a60-ada2-8d9e8bd38381",
      "created": 1644178039147,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006819",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "d98a8894-c811-43eb-9cec-8248f78ce816",
      "created": 1644163469963,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007393",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "cdaa8d90-2323-4466-8afc-4193bd2a2e60",
      "created": 1644149130207,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007417",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "7d21d963-76bf-4ae7-a3fa-9a56119451d2",
      "created": 1644134677256,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007501",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "f496702a-be5e-4bdd-be13-0f3b8d45cfb6",
      "created": 1644120208026,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007453",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "702b19ca-c375-40ff-a870-dc449f78929f",
      "created": 1644105806855,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007860",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "6327ddd9-6771-4ab2-bdd0-776e32027de5",
      "created": 1644091510294,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007880",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "6ebe0b38-a642-4ecf-9e19-b828b852d37a",
      "created": 1644077194342,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008217",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "0a3d72d5-3b7d-431e-98e8-a408c86fcdee",
      "created": 1644062859695,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007806",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "98653754-a4dc-4175-a7c5-ce5b0bca81f9",
      "created": 1644048300992,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007679",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "e41196b2-a0b0-4dc6-9113-02136b6d007b",
      "created": 1644033931016,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007696",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "a99aaaec-1b67-4d11-a357-4409b3be4eaa",
      "created": 1644019450047,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007584",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "e90db9fa-5eaf-45d8-a88e-4a90a438bac5",
      "created": 1644005192574,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008104",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "384d2f1b-2462-4348-9e04-38a799305d7d",
      "created": 1643990838563,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007978",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "82bee672-1de8-4951-8181-7e4fa041a50d",
      "created": 1643976402763,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "b3f6091d-0ffc-4e3a-9905-03f86dbda29a",
      "created": 1643962086895,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007792",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "e02029da-9aae-4d97-ace4-d06550f93f18",
      "created": 1643947629284,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007711",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "786342b0-bced-46f9-8611-c35efc5bf1d3",
      "created": 1643933060498,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007871",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "de23676f-76c6-4bab-a3eb-357b669f1a21",
      "created": 1643918838523,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007562",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "30144548-881c-40b3-969a-a986358d16ba",
      "created": 1643904324148,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007597",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "bb6a67f7-36fb-407d-b7e1-241fb6bc518d",
      "created": 1643889915293,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007759",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "bb45558d-d50c-4c21-9611-9f25c272d69b",
      "created": 1643875566027,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007434",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "964d8a00-a83f-4a3d-b31a-ffdefcdd56c9",
      "created": 1643860888842,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007706",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "faf0d143-f87c-4c9e-8ddf-0a905a02ca9d",
      "created": 1643846703781,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007671",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "ab179ed1-0f63-49e9-bb61-573a5ebbc295",
      "created": 1643832266898,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007569",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "867fc833-a6fa-4110-a31d-de27f2935061",
      "created": 1643817933577,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007476",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "3c5061f2-a7a3-4f65-bf74-db39628d3f3a",
      "created": 1643803614998,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007524",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "839a7687-6f5b-4378-aba2-9e9cf21aac4e",
      "created": 1643789242360,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007288",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "96e497c5-3f01-45b5-9549-046e57949fcd",
      "created": 1643774712383,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007552",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "f36cb83b-ca7f-42c1-b1db-b2bd27acdce3",
      "created": 1643760392965,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007783",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "be2927f1-79f0-41bb-ae86-c968c6998467",
      "created": 1643746007268,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007892",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "1a9be2b0-e722-45e1-b36d-eed0119d4627",
      "created": 1643731591264,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007898",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "b0ce2c64-e066-44de-a817-d23fa44fe836",
      "created": 1643717220407,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007257",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "01a1df76-2ce7-46fb-a44c-80cdec0d1059",
      "created": 1643702720931,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007594",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "1a010b9a-c243-4a29-b17a-1f30499f5858",
      "created": 1643688298354,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007389",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "c534e82d-ee2b-48b8-84c3-42cd24f0688f",
      "created": 1643674042040,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007588",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "a09f6696-f9a9-44af-9927-bf00c84e5966",
      "created": 1643659562059,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007770",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "2531560e-76a2-47b8-ae9c-f19005d5a161",
      "created": 1643645056252,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007407",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "8d1e2818-16ad-482f-a511-aa69ab23f567",
      "created": 1643630657271,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007363",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "30c7d35b-dd5c-4b1f-b3d9-804de037533c",
      "created": 1643616241009,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007338",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "0a6303fe-1122-462c-8075-859f9514c7ac",
      "created": 1643601864649,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007325",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "3b6a82a8-5576-459a-bbfc-d6f984f5cb94",
      "created": 1643587465921,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007668",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "fbf32526-12bb-4b80-b7e4-1b6b77f8ac9a",
      "created": 1643573016325,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007598",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "758b2701-db7b-4410-bf97-28abc2f49214",
      "created": 1643558714706,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007698",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "5d37449a-f654-4032-b100-6dbf69867e57",
      "created": 1643544213017,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007374",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "5ea44cdf-ed62-45d3-a1e5-d571403a1c3b",
      "created": 1643529879243,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007264",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "335910c6-fa74-423a-8399-193363865231",
      "created": 1643515414034,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007588",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "7ad7a8b1-17b3-4276-8505-4c63612b8789",
      "created": 1643501109825,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007607",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "8ca5b50e-ae30-4738-9650-2b6ce47f836d",
      "created": 1643486595938,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007362",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "99c2003e-53c8-46cd-a87e-f564b22542a0",
      "created": 1643472341006,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007519",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "9ed901ab-afc6-4d92-905d-5ac98fe1f2ab",
      "created": 1643457891268,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007339",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "b4c5e77f-483d-498c-abe3-c461580cb1d6",
      "created": 1643443495402,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007567",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "90570c3f-fe46-4c52-96be-cf66d667500d",
      "created": 1643429055274,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007726",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "38de6b75-aaea-4081-8f83-f6acf519786d",
      "created": 1643414656926,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007484",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "b3d2937c-dcd1-4941-a0e8-7a32f94c0808",
      "created": 1643400278126,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007381",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "b76bf5da-f188-4ce1-9e61-ca5abec88710",
      "created": 1643385981595,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007549",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "b06c511c-d1dc-4b3b-812a-f2289e491438",
      "created": 1643371651596,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007315",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "71376806-9332-4e31-beb8-8846cf900970",
      "created": 1643357010242,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007135",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "124c009b-7c64-4474-ac68-3c8c436ac840",
      "created": 1643342733197,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007202",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "9ce9b464-2d4f-4092-86f6-1774060ba899",
      "created": 1643328242724,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007367",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "4f13e8e7-b772-4575-a10c-f21423d8ce41",
      "created": 1643313804503,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007440",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "8338b987-4343-4d57-b9e3-a14fdd8eb740",
      "created": 1643299511987,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007400",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "c2034e33-2896-41a4-baab-98b77d401281",
      "created": 1643285155761,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006675",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "c0098478-c3bd-44ed-978b-c4059568dd59",
      "created": 1643270637720,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007078",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "e349c299-3198-4d7b-aa75-1f1e9477fe1d",
      "created": 1643256431106,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007345",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "d95ebf9c-2e99-428c-95fd-037e53f5e45d",
      "created": 1643241912029,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007439",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "fcf4d9e0-0b30-46e8-86d1-0a991e907106",
      "created": 1643227477738,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007538",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "72711812-8b73-4ddf-ae36-8667db2b8fb3",
      "created": 1643213232348,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007166",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "df5a8783-a2d2-415a-bfb9-9a35f281fe9e",
      "created": 1643198734647,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007194",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "5d112e0b-4428-42e4-894c-64e56e7e4720",
      "created": 1643184265850,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007072",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "4e8f10a3-5d68-4700-8d59-c742c5b69f83",
      "created": 1643169827957,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007055",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "5a886ba8-65f7-46a5-8102-2bec34b0ad03",
      "created": 1643155437347,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007629",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "3a6af1f9-661d-4dfe-86db-09717a68e077",
      "created": 1643141120736,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007392",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "6bfa0c97-0d19-46e0-9d8a-44fd47a18a58",
      "created": 1643126657887,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007599",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "9715f91c-622c-475e-bdae-878263f357a7",
      "created": 1643112388940,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007372",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "7e11cf9c-97d9-449c-bc47-d7a22f65ffbd",
      "created": 1643097971259,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007370",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "153b3d2c-acf6-4622-987b-f545ebc1afaa",
      "created": 1643083479292,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007301",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "ba720ce7-9746-44d8-b885-18167782dae2",
      "created": 1643069051415,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007298",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "2afa7218-d63d-4bc8-a317-593627a7ef6c",
      "created": 1643054723465,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007211",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "d9091f82-3e40-4826-b1b4-d96d92cb42a1",
      "created": 1643040934185,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007370",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "1892feb8-867b-4673-956d-5a0e33e9b680",
      "created": 1643026013501,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007787",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "2bbf2f90-9141-4c4e-89cb-c7ba57d67db3",
      "created": 1643011625863,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007590",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "ce32dac7-bd69-4745-9d83-5001d16eed0e",
      "created": 1642997134919,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007619",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "6742ac9b-fb3d-4b29-b00f-00b7459fcac3",
      "created": 1642982717220,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007305",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "2f40fa83-c0d4-4441-a560-5e0b06ee24a8",
      "created": 1642968379302,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007440",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "a5b38b70-b932-4271-adaf-378509516cf1",
      "created": 1642953950444,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007467",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "9f21be93-8fa3-4bdf-9913-09e2a74a1034",
      "created": 1642939476987,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007674",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "a4fa1635-931b-4925-a017-22834507d6f3",
      "created": 1642925081234,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007363",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "b0a4a0eb-7137-41d8-a52d-88b688d6f34d",
      "created": 1642910651921,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007035",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "137a099b-640b-4760-877c-e29ee58e1747",
      "created": 1642896242222,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007480",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "1e0752ac-ea5d-4079-93a8-4b78bbbd8129",
      "created": 1642881850873,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007470",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "f60fca26-a815-4e11-8069-26e05105e434",
      "created": 1642867580141,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007359",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "72ac9ad4-9c69-4cd2-9151-c424156df6c6",
      "created": 1642853177202,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007943",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "3f56a180-c344-4734-a525-4f5bc3c8e7be",
      "created": 1642838619775,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007801",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "b1cb1eb4-a218-4f53-a189-fe9868908c0f",
      "created": 1642824198386,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008525",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "a7964a03-c900-41a1-9ec5-044b419168c5",
      "created": 1642810007154,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008514",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "e4006400-da66-41a2-b81e-6ee73ba4e731",
      "created": 1642795530294,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007934",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "45e46141-139a-4c80-abe3-a52c85ff9ee1",
      "created": 1642781061209,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008194",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "7171ef8d-2732-4ec8-a0c3-115b24c1589e",
      "created": 1642766874222,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008133",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "5bec4451-f87b-4b7a-a699-6dba924efd8d",
      "created": 1642752284871,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008056",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "5212afde-42d0-4164-b2e8-aaa762460ab7",
      "created": 1642737965729,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008413",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "f13002a0-f9a1-4580-bc2b-3ee317e1ed47",
      "created": 1642723613710,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008437",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "55787aeb-bf5d-4374-99a9-a8d1f3f7196e",
      "created": 1642709171845,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008439",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "a3ca4f12-77cc-4700-a5dd-1d6d15fa7aaa",
      "created": 1642694818338,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008289",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "e9497cd6-e8cf-459d-9529-5ef9921a8550",
      "created": 1642680302782,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008329",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "d21421b8-cd3d-4d8b-92a3-3093f15d8d0b",
      "created": 1642666136904,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008060",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "b45f00d0-07b3-4b3e-a8db-2ce813614380",
      "created": 1642651574783,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008018",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "4d684312-18ad-4155-a39f-3dedfc0ffb18",
      "created": 1642637206167,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008114",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "d7a0b4b5-91c4-4b1c-a910-f56c7e79c353",
      "created": 1642622722479,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008199",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "3da7687f-667a-4812-86a9-4642446c9e7b",
      "created": 1642608414890,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007875",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "77138a69-0342-4405-8986-26aadfbbb16f",
      "created": 1642594080241,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007832",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "6e4f5027-3baf-4018-a70e-62d0a2aa28e5",
      "created": 1642579612281,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007620",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "2f14f25b-bea3-424a-9454-0bc17ced1c2c",
      "created": 1642564938952,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007788",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "b6d9a272-f0e6-44a4-a077-a6e4be3b0baf",
      "created": 1642550748541,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007693",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "6f3048e7-7e2c-4a53-a989-6f5cc44b7e66",
      "created": 1642536306625,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007897",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "fcfe9700-6c77-48a1-9381-5b47f1fb8ecb",
      "created": 1642521924349,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006794",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "ced11e39-ff29-415e-8733-4c1ba23e01a8",
      "created": 1642507521380,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007761",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "8a2b99c0-6996-4f6f-af2d-fa2087abf802",
      "created": 1642493298869,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007343",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "199e7b9b-0b4d-4302-b99e-38f454591d81",
      "created": 1642478639757,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007592",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "70ccb1c5-2a06-467f-ba88-fe65ebc189f1",
      "created": 1642464171813,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007855",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "c50251a9-a317-4c72-b9a3-b687a886b111",
      "created": 1642449978246,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008268",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "8dbfd9a3-4005-4d70-a3f5-6622edc53750",
      "created": 1642435539050,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007985",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "e5446957-dbea-4f16-86f6-70aa26faba0a",
      "created": 1642421006498,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007885",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "1c4eeee5-8326-4dbe-8a55-53dbb0b50c55",
      "created": 1642406729979,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008427",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "b61c1ceb-8d81-494b-8bd2-3793d3c3e866",
      "created": 1642392359734,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008694",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "09e58367-6e02-4530-a19d-44f45d858f04",
      "created": 1642377934456,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007903",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "31e632b6-a31b-442b-ac79-8c17c481cbf0",
      "created": 1642363461145,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008468",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "ba204ff1-41ef-4f1b-ae4f-6fca76f7788c",
      "created": 1642349037957,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008179",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "d9a9f6b9-4d98-4b1b-b6f3-e7357e612f2d",
      "created": 1642334692763,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008290",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "a14e7a5b-d2f7-4d35-821d-4011beacff88",
      "created": 1642320300911,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008450",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "86ca1f11-7406-48ec-872e-40d9238b995c",
      "created": 1642305822508,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008127",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "fd145f59-7c6d-4612-b5e7-87aabaf3883d",
      "created": 1642291521733,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008018",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "1b9f8bb9-3409-466f-b24f-cfc536f8c383",
      "created": 1642277108577,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008615",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "03cdea32-2bf6-4e88-b7c0-e2d5696613d4",
      "created": 1642262667845,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008491",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "606150ba-8a83-4026-958a-77f91c33726e",
      "created": 1642248412032,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008724",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "438d2b7d-44fe-4f42-be71-a5008d122e50",
      "created": 1642234081768,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008554",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "6093ef78-a624-4ab4-84c5-8abe204a5c1f",
      "created": 1642219377447,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008921",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "0e534ef7-08eb-4b4a-b7a3-9e4146199397",
      "created": 1642205102364,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008694",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "9e35d329-a97f-4dcc-9aaa-3dd1f666ae37",
      "created": 1642190717468,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009010",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "b53aeb6f-a6ec-4ac1-b298-7ea042bd3488",
      "created": 1642176298250,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008685",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "05e40de7-d085-4ef5-b9b8-fd21105e2dbb",
      "created": 1642161829339,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008291",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "a452c118-24fe-43bd-9f97-15a867ce4d7d",
      "created": 1642147397569,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008270",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "b448cacf-a862-4f58-9730-7639c352d36f",
      "created": 1642133295435,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008375",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "c7ad4de6-a25f-4c2b-988b-b669d2754963",
      "created": 1642118636538,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008550",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "64332c3b-aafc-414f-bcb8-84de55f4711a",
      "created": 1642104401725,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008507",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "7b61e51c-a259-4050-b9dd-14739c3ef281",
      "created": 1642090035434,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008623",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "6c8d328e-a296-47fe-9262-88272c677fcd",
      "created": 1642075567540,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008252",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "77c3b83e-2614-4a60-aad0-5c18fce7efe3",
      "created": 1642061158862,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008383",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "3b525dbe-2786-439d-abd2-2d87431ec87e",
      "created": 1642046598291,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008633",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "4624bbfd-d4b3-480f-b353-2c30869de979",
      "created": 1642032203368,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009411",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "5f897921-7693-4746-8170-832c04b53ac6",
      "created": 1642017954666,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009198",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "fa775f56-9208-4d2d-8608-dc8baaae4d26",
      "created": 1642003456410,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008636",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "8f93eaee-cbe6-4354-b800-01e1260bbd7c",
      "created": 1641989301155,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008245",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "48518693-8cd0-4741-b9a8-e7e66e1ca5b7",
      "created": 1641974796242,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008341",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "a67be599-790c-4c87-93ce-15b3c616d809",
      "created": 1641960258311,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008563",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "e3e7fc84-52cd-4c85-a354-79a9a0fd6203",
      "created": 1641945979249,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008419",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "8a5dde55-b5ac-4de6-81cc-3da5236c81a9",
      "created": 1641931493768,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008563",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "1d2fe4ad-20ea-4c94-8fb5-2522e76ab4d1",
      "created": 1641917103173,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008842",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "dd171ff4-1141-477e-9049-79f1d077a374",
      "created": 1641902588277,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008886",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "7b69be1d-e6fd-4f74-adb8-055e09f0bde3",
      "created": 1641888330545,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008695",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "3f51b442-cd44-480e-91d4-0bce61cbd8a8",
      "created": 1641873971895,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008307",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "67704492-5f34-4c63-9abf-3b84f04295ad",
      "created": 1641859338605,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008556",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "b6a6e92e-dd34-402f-b217-8f791d58d027",
      "created": 1641844966156,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009045",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "49cb1480-d993-47fe-80fd-645d490482e9",
      "created": 1641830704913,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009186",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "5598aa98-351a-4669-ade9-956dc9c8e1fe",
      "created": 1641816511515,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008759",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "914a22b9-2170-48bf-81f9-bc092e1e658a",
      "created": 1641801870839,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008328",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "bb3f7ea4-77c9-4aab-986a-d6e6d6f1dbd0",
      "created": 1641787319216,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008547",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "09474af8-f79d-4d9a-a08b-eda995aae0fd",
      "created": 1641772946154,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008710",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "17ac8039-34cc-42e7-a3d8-79d6e89c248d",
      "created": 1641758559094,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008307",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "d6cb85ec-05f2-499d-a1dd-d2dc1dea239a",
      "created": 1641744090527,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008138",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "ec59187d-6a29-4a89-8e5d-268cf427f20e",
      "created": 1641729820968,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008243",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "884f95e7-d71a-488b-88c4-4d9cf39b5fac",
      "created": 1641715278027,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008177",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "86916365-2b27-4e4e-b2e7-c0ce6d634b96",
      "created": 1641700918019,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008178",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "e8518b10-15e9-4596-8489-84683ba222d2",
      "created": 1641686477519,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008380",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "1542078a-3187-46a6-a4b4-b16a3e89bc6b",
      "created": 1641672034011,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008891",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "a455db40-d15a-46aa-aaa5-27945cabb3e0",
      "created": 1641657720644,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008889",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "fda7a878-fb92-4c44-94a4-909cd68f8276",
      "created": 1641643469223,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008772",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "f28ab015-e5f8-445a-b2f9-475bc3864d29",
      "created": 1641628871395,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006370",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000127
    },
    {
      "id": "c727d2c6-449c-4b0b-b0c1-43eed2b1ff31",
      "created": 1641614520890,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006450",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "80181638-7dab-49bf-abe6-86fdafb1d4de",
      "created": 1641600090886,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008048",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "a756b864-08e0-4fc9-9a23-c6b17bf57ad3",
      "created": 1641585681866,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008750",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "21cb9960-f9f2-480d-ad91-05461b45848b",
      "created": 1641571316684,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008027",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "71a9f2af-c560-4fec-bb4c-e2a0448988ae",
      "created": 1641556892864,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007987",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "92dc8f1e-d4f5-4657-9424-6fb2cacdfe97",
      "created": 1641542533903,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008681",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "8714afda-79e4-47db-898e-8e9dd97dcab3",
      "created": 1641528098362,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008246",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "27711c28-3a49-44dc-b3c2-672fdc7bd6df",
      "created": 1641513737902,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008384",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "9695abcb-3d7a-44d8-82a1-0526c9de5d15",
      "created": 1641499341508,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007929",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "63538417-823b-41be-92a2-e56a7c2fc106",
      "created": 1641485092390,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007966",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "06f98914-1128-4dfa-a695-c5bbbfa398fd",
      "created": 1641470523151,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007997",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "29470630-c376-4562-9964-9eb56830565f",
      "created": 1641456063841,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008765",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "e2b15073-218b-42ac-932a-37399c044217",
      "created": 1641441653349,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009002",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "56016069-801a-4e05-b663-5179ea96bdbd",
      "created": 1641427260019,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008650",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "38697d64-478e-4780-ac30-070a68602031",
      "created": 1641412860836,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008723",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "b3945f1d-5745-4ae4-b101-de4c21c6ce95",
      "created": 1641398690839,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008500",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "88ea17c7-e368-4ba2-a163-1465167b54e8",
      "created": 1641384270909,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008043",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "1a7b1ba4-a1eb-4590-b4b9-252c2404b7e8",
      "created": 1641369837152,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008139",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "45d02d12-2f4f-45e5-a1d0-ce50d662d1ad",
      "created": 1641355416678,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007582",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "62692b97-d53e-427a-b403-16b49a9efc5f",
      "created": 1641341194708,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008554",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "0a716c22-60c9-453e-b52e-705029415ca1",
      "created": 1641326696537,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008674",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "99514776-07f0-489f-ad6f-0f20feeac212",
      "created": 1641312454500,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008770",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "3070bf20-4816-4584-b5da-8f9dcbad9067",
      "created": 1641297926477,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008810",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "9397908f-25e7-4073-bc98-9f23e0533814",
      "created": 1641283493845,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008781",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "5c5f2a2b-7ed4-4b9f-b90b-69a04bd6e49d",
      "created": 1641269224786,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008656",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "fb565dc4-62a8-4041-a89e-35746e7044a3",
      "created": 1641254616441,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009090",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "6e1912cc-88ba-406c-8b37-0c014c876578",
      "created": 1641240251020,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009208",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "106da64d-dc81-4405-8ad4-c852f42d5699",
      "created": 1641225959987,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008953",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "2452f70b-c54b-4f79-bf33-4d6ea426f865",
      "created": 1641211490611,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008961",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "e8729efc-57ac-4d66-9453-1f81ebe799fe",
      "created": 1641197179682,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008998",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "42607490-258b-4161-9297-d0f5ec851537",
      "created": 1641182711124,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008979",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "2feadf8d-8ac7-435f-b505-bb1aaba8a156",
      "created": 1641168193738,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009127",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "d7ce4133-cff5-453a-82a7-b9d9316c841c",
      "created": 1641153839756,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008510",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "4aec5a6b-0742-400d-bd23-c0255f218565",
      "created": 1641139416830,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007693",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "773c99b3-c56f-431d-8d54-8aeeaeff5b1b",
      "created": 1641125105282,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007728",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "8bfe7b51-bb36-4aef-8776-975c5b1f860a",
      "created": 1641110664039,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007872",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "a50ee6bf-32ee-4ab8-a4c2-eee5e4882b6b",
      "created": 1641096207026,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007698",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "f7dd657f-1914-4e2d-85ee-71c200032970",
      "created": 1641081784079,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007684",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "a21a756a-9d80-416b-b46a-088308350e26",
      "created": 1641067393137,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007614",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "d4405be4-e4c1-4b0b-b5aa-95bbdd0101f0",
      "created": 1641052980212,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007477",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "eeb03da8-af65-4ce6-a6cf-93bd32dcf737",
      "created": 1641038702849,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008387",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "43cccdae-9d03-4ac8-8331-4d4c28443e3e",
      "created": 1641024271948,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008589",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "95d0f745-9ad0-474d-8507-f9c7e1308868",
      "created": 1641009842020,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008890",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "bca0122a-02e9-4243-8bbf-bfaa257f13fc",
      "created": 1640995366895,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009110",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "6febb26f-d417-4e70-bee1-9bd02c874ac6",
      "created": 1640981060010,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009286",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "b1be4940-27b7-461d-a8bc-e4c8b408a252",
      "created": 1640966633766,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008985",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "1d6e151f-a629-4ea2-b8bf-df2178cf5b2a",
      "created": 1640952255518,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009368",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "834e3805-6200-4323-8c82-1fdba3a197a9",
      "created": 1640937993584,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008810",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "644384c6-476d-4eab-ac93-9ea088a991d3",
      "created": 1640923464733,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009079",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "518995fd-fc14-4864-b077-c17b4361da78",
      "created": 1640909073138,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008978",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "4287459e-d28e-4189-af4f-8e46e5f0a670",
      "created": 1640894656351,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008891",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "bd20921e-7ddc-4fd6-a3aa-90052d083552",
      "created": 1640880200081,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008365",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "4e4b7712-89b8-4958-ac70-e1b0b1aebf56",
      "created": 1640865947039,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007811",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "2628f10f-d9b8-4bbc-80df-47fae065b613",
      "created": 1640851409180,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008235",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "ae44575f-24cf-4fda-960b-521645d6650f",
      "created": 1640837067887,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008057",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "e2b8c432-0958-4cae-85dc-d597719e5e78",
      "created": 1640822703547,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007938",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "ea15e7a5-6bcc-4408-985f-c40e6ada49d9",
      "created": 1640808296323,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008571",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "41f42c29-192c-4c6d-ae12-524853511d5c",
      "created": 1640794110546,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009205",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "f45306ad-eb91-4616-98f0-5415b4901ed9",
      "created": 1640779520480,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008926",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "17ac67f7-e2f1-45f5-a90f-83c1a365036c",
      "created": 1640765091248,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009754",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "b92efc40-4250-433a-963f-fddf41442181",
      "created": 1640750910388,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009344",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "e4a19e9a-b5a8-4fe7-a763-5930a24290e0",
      "created": 1640736265965,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009342",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "254e725d-2187-4742-adb1-ae8465471998",
      "created": 1640721863140,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009318",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "fa18a99c-aa7d-4682-b689-12a16267b8c6",
      "created": 1640707431119,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009223",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "bd4b6c51-a41b-4a81-8a5f-d5846868a230",
      "created": 1640693107071,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009531",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "edfc98f2-5107-4fd4-958c-061699c9c974",
      "created": 1640678779099,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009583",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "7ca7ccc5-4ff7-445a-b706-c00b52882b60",
      "created": 1640664313743,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009138",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "a46ffb69-99cd-4415-bc23-c629a88a7ba3",
      "created": 1640649912232,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009125",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "9066301e-f929-4c75-916c-8512a19723f2",
      "created": 1640635488260,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008649",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "d8f361b5-c3e0-4d64-a770-21492863a81c",
      "created": 1640621064943,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008042",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "bf483d0c-978e-4cd7-9891-0b23589f849f",
      "created": 1640606788374,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007311",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "77758ca1-939f-483a-9d57-14c0ba9889f5",
      "created": 1640592341489,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007476",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "8fa18550-e266-48a1-b3b4-1eebedc6f9f0",
      "created": 1640577998510,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007726",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "89b7cf04-2738-4dc4-a9d6-7c7609b35023",
      "created": 1640563480516,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "ff964e74-edae-438b-a684-6f6be5656a53",
      "created": 1640549056686,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007907",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "a85ee804-fd0c-4c96-b6f8-25ae9422296b",
      "created": 1640534708906,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007875",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "8f55fb40-ceb3-4a3b-89c5-56f88e8ff6d1",
      "created": 1640520291474,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007631",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "9803ef00-b654-411f-914b-248a7c63956a",
      "created": 1640505869947,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007873",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "31987c16-d91a-4be6-81a2-58d1579a308f",
      "created": 1640491490650,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008036",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "b35a6754-5412-4b37-926e-6b0f64a28829",
      "created": 1640477048365,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007338",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "86396b76-2b20-481d-a4ec-2773ef311cdc",
      "created": 1640462741680,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007934",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "2fd8366b-fadb-44b8-b964-a9f8aa09e014",
      "created": 1640448204758,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008872",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "93071f3f-b137-4d45-93a6-4d667c6f1000",
      "created": 1640433914732,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008502",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "bc1a6686-ccdc-4c5c-9104-840baa15b403",
      "created": 1640419560438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009108",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "592086df-9475-4438-9591-5b368ea2d1f6",
      "created": 1640405066552,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008828",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "65ddf9bd-3872-424a-9090-c145205f027e",
      "created": 1640390786304,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008791",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "f6637f38-8168-46d7-9736-65a62a6f2580",
      "created": 1640376265373,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008883",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "77d3f94b-c2d5-4fb5-95cd-d9a6c61bcaea",
      "created": 1640361987877,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007376",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "cc535250-d6a8-4d3b-ac0b-3f840840f0c2",
      "created": 1640347421303,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007696",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "87ebc2e6-1beb-495a-aba7-883404f99fb4",
      "created": 1640333116444,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008192",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "4c020b2f-37e8-4127-b351-beeceade6a29",
      "created": 1640318709028,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008170",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "d4799c37-f167-49ed-933c-31ee3c147d3e",
      "created": 1640304239393,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008002",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "196fd21f-36bb-456c-b5fe-136359f27b4d",
      "created": 1640289832827,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008383",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "cbeaa7db-071e-400c-b3da-b59fe38ec4a1",
      "created": 1640275537335,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007495",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "325f3bdb-f5a3-4ec0-9a5a-85085fdd6b5b",
      "created": 1640261025917,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007230",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "de59e3ea-dfe5-4f63-8269-35d12d6305ef",
      "created": 1640246713692,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008717",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "aed3b002-6566-4955-abb3-3b4faa6c7af0",
      "created": 1640232248419,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009176",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "a3917e67-257f-40cd-ad27-fef91c59c9a6",
      "created": 1640217818388,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009171",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "4f34a055-5b5d-4603-a4ec-4fe633dc987c",
      "created": 1640203415338,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009059",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "05877fc7-4660-4706-90c4-e7e85f4cdbb5",
      "created": 1640189096389,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009210",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "646dd0e3-70eb-45c6-a99a-3917e97ecb4c",
      "created": 1640174723239,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009486",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "20b1def3-8bef-4e3e-b0ec-ecef9341c6d4",
      "created": 1640160365641,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009080",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "f7526e0d-b613-4fa4-a347-c9ef480b83a7",
      "created": 1640145879017,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009420",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "f4728794-4a69-4fd1-8d97-b721f224c0e7",
      "created": 1640131722272,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009117",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "d2b0f6f1-c3e6-4436-ac8b-3c49518a3f93",
      "created": 1640117129792,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009437",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "91b9ed7f-7f14-477d-82ba-08ef1c5141c3",
      "created": 1640102729094,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008932",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "876b8a7d-f795-418b-aced-2d78bf19f397",
      "created": 1640088473755,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009287",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "f376e1b1-210f-4644-a270-e53d7244cbbe",
      "created": 1640073931729,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008797",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "f68440a5-1165-4826-9032-baa0dcdbe504",
      "created": 1640059442591,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009201",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "dea77038-b507-4043-978a-844dab9fc536",
      "created": 1640045100185,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009414",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "0ba30d69-209c-418c-8ad5-cfa86e004f55",
      "created": 1640030748814,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009688",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "ecf52386-5f22-4759-b678-7c1086881486",
      "created": 1640016462716,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009127",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "0a01ad08-61b7-41e6-a247-724a1050289a",
      "created": 1640002044876,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009418",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "62c25e03-166a-4ac8-b023-62be7cec1ef6",
      "created": 1639987491565,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009716",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "5af706cd-d674-4354-bdf3-63feedbdcf83",
      "created": 1639973020342,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009642",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "61af1231-49ff-4b33-9df2-dcd822f8b2e2",
      "created": 1639958620169,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008473",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "a3fdb520-3574-4ad8-9016-cc951b9c0d05",
      "created": 1639944313881,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007420",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "5adf92e8-eda9-428a-84e2-dc4badd6ae10",
      "created": 1639930023534,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007888",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "9972811f-dcfd-4d85-952b-51f6f9261b3f",
      "created": 1639915422725,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008180",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "4c1b2c82-1452-43b5-a903-86c39d09de33",
      "created": 1639901080719,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007635",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "9c52a8a9-89b3-457b-9b80-056fdc390ff8",
      "created": 1639886768308,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009930",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "bfd4b6f7-a154-405d-9971-d8dd61706004",
      "created": 1639872230566,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008015",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "f3516925-d709-4c0f-a01f-f009f9b77cb5",
      "created": 1639857805594,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008153",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "a9f1c4ac-d6ce-419a-9c1b-143d497cbb2b",
      "created": 1639843426768,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007634",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "19dc81ef-fa05-4bad-9f0d-2c66ce482be7",
      "created": 1639829163495,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007368",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "0d7ef217-fed1-4651-97f8-96cb150dca85",
      "created": 1639814789685,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007401",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "2d4cc38a-a782-40d6-9731-1e0071139f5a",
      "created": 1639800233669,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009175",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "817775dd-af48-4588-a63b-15b9f6f14ddb",
      "created": 1639785948806,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009575",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "3b0f6ab4-059f-4533-b7f4-a1fe65a646ae",
      "created": 1639771544593,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008955",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "76ffbe70-24e5-4d7a-b498-07e3293b1b55",
      "created": 1639757035470,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008527",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "2ba36b7e-70bd-48b2-b641-3ebeaf3775eb",
      "created": 1639742647222,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008839",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "964ccd87-8dab-4b07-baa4-589ca0491d50",
      "created": 1639728236658,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007789",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "527cb391-a6e2-4c66-b4c6-b5cff8f94379",
      "created": 1639713825746,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009454",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "370d20c8-af3e-4c70-87e1-36db129e2566",
      "created": 1639699478653,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009780",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "0567ac7b-078f-4912-977f-e845581714dc",
      "created": 1639685049497,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009552",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "0fcc62d7-c886-4499-ad91-52d3d57a4174",
      "created": 1639670645562,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009304",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "a165a46b-57fe-473e-a7ce-f188f49fa910",
      "created": 1639656238890,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009158",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "e6c271ee-a951-4f6b-bfe5-74c41a2907b5",
      "created": 1639641883260,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009536",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "73933f19-bb86-4f29-b452-ed94f50fddc9",
      "created": 1639627493318,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009605",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "f47c75ff-2574-4dd7-ae49-d03a6ac86f09",
      "created": 1639613055435,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009801",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "85d909eb-8199-44d7-80dc-341d396f070f",
      "created": 1639598615553,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008947",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "dfefdd78-16ab-47c5-8564-055947b94a44",
      "created": 1639584225932,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006999",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "62609dbd-14bf-4434-bfb0-f9ee1117c3a0",
      "created": 1639570044925,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007054",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "e5bb102b-ed1b-404d-95cd-5b4713154114",
      "created": 1639555485585,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007403",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "dd52aa3d-ca19-493a-9776-525fd52c6920",
      "created": 1639541034659,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006944",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "92b2074b-bf33-443d-9e9e-6441385acd0e",
      "created": 1639526670010,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006944",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "148aead1-964a-4bb2-80ec-4698695f2d13",
      "created": 1639512408745,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007300",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "7a435365-d048-45c8-a9f9-82cd6d574f1b",
      "created": 1639497974591,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007415",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "9f508fda-933a-48a4-9218-d8f2b62f736c",
      "created": 1639483673065,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007184",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "3eb485a4-26ad-438a-811b-5a3a0ce712ae",
      "created": 1639469186628,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007220",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "c792bd3c-a86d-414c-b61a-a807b691bc37",
      "created": 1639454660988,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007046",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "b9349752-588d-4471-bac2-edfc6dbdc92c",
      "created": 1639440236258,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007181",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "a1a48137-a56c-4b1f-8dd7-f433e30f4d84",
      "created": 1639425945674,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007821",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "0fb3fcb3-73a6-4430-b8ad-af854b8ed93f",
      "created": 1639411445237,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003891",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.8e-7
    },
    {
      "id": "bc5c4e3a-ce45-4aa3-a274-ce8eeef3a020",
      "created": 1639397101531,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003221",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.4e-7
    },
    {
      "id": "f19b45aa-f691-4d3b-8803-b5381c3ac145",
      "created": 1639382665339,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003244",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.5e-7
    },
    {
      "id": "f6e2e502-f62a-4102-a1e3-37a90a9a48d7",
      "created": 1639368243379,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003164",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.3e-7
    },
    {
      "id": "2781117f-50f8-4006-b638-30369f961af5",
      "created": 1639353801787,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003510",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7e-7
    },
    {
      "id": "fcba4885-7a5e-42ca-9585-d963b6a845db",
      "created": 1639339420883,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003207",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.4e-7
    },
    {
      "id": "16ec4dff-c519-4cf2-8b83-e4a5189c9438",
      "created": 1639325030201,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003365",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.7e-7
    },
    {
      "id": "96f839a8-459f-4910-b743-d668a25a7b9f",
      "created": 1639310610118,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003406",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.8e-7
    },
    {
      "id": "39d46f3f-3aa6-43c2-9621-dd9537fdfb0e",
      "created": 1639296594251,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003273",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.5e-7
    },
    {
      "id": "e48822e7-dd18-42c9-bcf6-c9d60ce03d58",
      "created": 1639281928141,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003135",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.3e-7
    },
    {
      "id": "b891c508-8ea6-4f12-86be-137bf35d9d15",
      "created": 1639267405692,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003457",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.9e-7
    },
    {
      "id": "140a262c-adbc-468f-a72d-c0ef5a3795e4",
      "created": 1639253054548,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004033",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.1e-7
    },
    {
      "id": "f627fcc9-3884-49e4-a96a-69a810a6f7d9",
      "created": 1639238674898,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007144",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "7a006c19-9850-4ce9-9f2d-e4492e8ec7ca",
      "created": 1639224244887,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007777",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "f83bc9fd-87fb-436e-a56c-f543c8344863",
      "created": 1639209806911,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007715",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "fc6a05df-184a-492d-b603-a19d239b3679",
      "created": 1639195462244,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007471",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "3bac39a1-277d-4d4a-b71a-d804567837a4",
      "created": 1639181132237,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007733",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "fd454708-2fe8-484f-817e-46fbfbb0c194",
      "created": 1639166694585,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007894",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "6a6fc15c-ce67-4e56-9d70-a9f3f07169e4",
      "created": 1639152239483,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008250",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "56b1d13e-dc1e-4f05-82ea-b840a28319c6",
      "created": 1639137839780,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007967",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "b870f69b-3de3-4923-b4b7-215528088230",
      "created": 1639123431634,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008127",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "5647c612-bc05-49b6-8d06-4d86d250c3c1",
      "created": 1639109034657,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008033",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "589fe6e5-04b2-4754-bc5a-2166f2133748",
      "created": 1639094615892,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007478",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "140f0f93-69ac-4d7e-96f3-769da17edfed",
      "created": 1639080194619,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007827",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "79676605-4b4e-49ad-ba02-d7975f26db84",
      "created": 1639065836159,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007655",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "ea6ff310-3885-48a7-94af-af8d7c13f461",
      "created": 1639051560435,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007897",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "7e7af2d7-87b1-40e9-9d1a-077247d1221a",
      "created": 1639037064318,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005609",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000112
    },
    {
      "id": "59274239-828e-464b-9eba-dab66eda06f9",
      "created": 1639022627605,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005494",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000011
    },
    {
      "id": "3bac3028-1a68-4450-8134-5c8a1a116b2d",
      "created": 1639008307452,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005274",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000105
    },
    {
      "id": "bb0f77d3-65e9-4ad6-bb97-af6e3117d139",
      "created": 1638993963769,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005516",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000011
    },
    {
      "id": "aff932b8-75a4-401d-a2ab-be23f1e07dd1",
      "created": 1638979455421,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005205",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000104
    },
    {
      "id": "b87f94ca-0b5a-479f-af72-ddd7dc0a91cf",
      "created": 1638965060888,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005228",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000105
    },
    {
      "id": "019e1a4a-a571-456f-90d2-cffa25e04bd3",
      "created": 1638950633058,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005070",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000101
    },
    {
      "id": "cf18497d-4740-435a-a42b-8e6d37ca4ff9",
      "created": 1638936230402,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004974",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.9e-7
    },
    {
      "id": "7ba985fa-e1e3-42d1-8287-964a7e58e8ce",
      "created": 1638921903545,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006876",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "b16327de-5430-4c85-93c3-3653d201ebb5",
      "created": 1638907574637,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007388",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "7c8ea04d-192a-4160-ae5f-e234706e29f4",
      "created": 1638893015576,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007485",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "9d24b586-6ef6-4bd3-a5c6-8197f3a265a6",
      "created": 1638878665214,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007627",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "0928adce-422d-4e19-827b-95c6353ba5b8",
      "created": 1638864514808,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007480",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "8bb83da0-4921-4886-8a56-ffa4fc8c78ea",
      "created": 1638849826925,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007562",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "d01b7abe-40e5-446e-ba85-270c6fb72d3f",
      "created": 1638835579109,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007814",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "84236e71-2279-49b3-a3cc-e31ed785aae5",
      "created": 1638821112556,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007535",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "82482c92-205f-46b1-8291-b72998277cef",
      "created": 1638806669233,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007457",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "db0480da-3b86-4c63-a30c-776b68e324b6",
      "created": 1638792350733,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007454",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "a151a038-925b-4166-862f-cc9ab1212cbe",
      "created": 1638778060188,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007749",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "4cc24b24-4d90-4990-ac65-cf9d79389561",
      "created": 1638763409185,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007717",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "587f9136-d7b6-4c20-9bd9-79a04c1e03bc",
      "created": 1638749127785,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007190",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "ed8eb514-e9c2-4d78-8c2d-e08caac45473",
      "created": 1638734686827,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007469",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "c5c74aaf-eff6-488c-a1ee-db5c015998e2",
      "created": 1638720255526,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007599",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "0a5ada61-8c5e-4e99-a4c1-d831c8cd1544",
      "created": 1638705911603,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006986",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "4d94772f-8d59-483e-a5e6-132ed9050e44",
      "created": 1638691466290,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007281",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "33c65682-032b-4649-ae1a-0bed855ad50a",
      "created": 1638677099883,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007964",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "171bc37c-44b3-4197-8740-44235e553134",
      "created": 1638662698247,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007748",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "b2085807-b1c8-4418-b38e-a947655763c5",
      "created": 1638648264748,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007749",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "a8ffa793-9b58-434e-b99d-e9465b361823",
      "created": 1638634008627,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008020",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "cd835f43-3ade-4b2d-bbb4-04049e01ab00",
      "created": 1638619523581,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007814",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "8ec94dd4-9433-4131-93a4-e9c83e391977",
      "created": 1638605040313,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008173",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "193d0619-ac67-4e25-95e3-7a3104187c7d",
      "created": 1638590701439,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006990",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "23ba7169-43f2-474b-bb75-e594a75ba35e",
      "created": 1638576312930,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007500",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "33251dd8-3563-440b-af4d-c3a9fbed6055",
      "created": 1638561874660,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007479",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "22a01736-96c3-4dff-8162-56a9d364c767",
      "created": 1638547533733,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007452",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "53db853d-b3ed-47cd-b8f3-90c3341bb00e",
      "created": 1638533232341,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006983",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "b439f8a6-5b93-470a-ae1e-63be485638c3",
      "created": 1638518761591,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007178",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "7ea25b05-92ef-4a54-8538-9e7d7be4639e",
      "created": 1638504389577,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007308",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "76652319-e6db-452f-96b8-450aafa64778",
      "created": 1638489962088,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007003",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "f584bddd-3908-48f0-8bef-fe3a9d2baad2",
      "created": 1638475711165,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007135",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "718f4cd1-40e9-4396-85f5-0a6130382731",
      "created": 1638461224635,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007171",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "f4ec7438-b46d-4052-a4bb-2540fe26edb8",
      "created": 1638446972206,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007030",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "81dd5cb5-7164-4d37-9815-702582904047",
      "created": 1638432432802,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007197",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "c1946af5-62d9-44e2-a4f4-c0a1f9b5f41c",
      "created": 1638417924145,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007790",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "bb31ec4c-eb7d-4590-a462-84a3d66296b5",
      "created": 1638403405571,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007651",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "e2a87594-c101-4c1f-9108-47a860197d68",
      "created": 1638389016701,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007280",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "b3266b96-b44e-4710-b266-0adce12fe319",
      "created": 1638374734031,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007715",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "ebb15454-9311-44af-9926-6a6b7da56294",
      "created": 1638360263621,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007651",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "7adb5c85-3af3-4d8e-b59e-b3bc7512787a",
      "created": 1638345836865,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007613",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "694c78b2-3299-4dcd-a7db-e67de67d0f34",
      "created": 1638331517650,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007897",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "fd3ce8f0-3053-4290-a2db-babd445a14e4",
      "created": 1638317061845,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006890",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "89971a1d-254c-46ad-b051-69d1d9aaacf9",
      "created": 1638302742466,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007594",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "395bea29-67ca-46da-85cb-5931d8c0710f",
      "created": 1638288325496,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007305",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "1444d2e9-8a03-4191-b4b2-f263bc9f251f",
      "created": 1638273867869,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007648",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "57790515-ff2e-43f5-b65f-0af15a630a26",
      "created": 1638259238636,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006621",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "69c53677-2ea9-4387-a743-2f6f317c4127",
      "created": 1638245049670,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007470",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "0681416e-3236-403e-9474-8fb6b7dbe007",
      "created": 1638230563992,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007246",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "84ecab60-b6b9-4b56-883c-0e15094209f0",
      "created": 1638216251995,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007060",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "bc5a0832-eedb-49c2-a59d-57662777b20d",
      "created": 1638201830180,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007102",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "83a81311-0c9e-444e-b8d7-0b8e505c4b59",
      "created": 1638187604769,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006843",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "14f3986f-a240-4b68-9c28-237e3f03a6d9",
      "created": 1638173097906,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006936",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "e65a3698-592a-4d61-99ec-7fb8bbe0249a",
      "created": 1638158691456,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006876",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "83a0fe61-bc32-4180-a12f-c0e22fe8159b",
      "created": 1638144260521,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007116",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "9d7a522a-feb5-4bbc-85a7-b5a13703e63b",
      "created": 1638129808514,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006947",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "378b2b8d-1912-4e71-842d-7d0ff5bfc261",
      "created": 1638115419436,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007052",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "681e8068-6977-4ad2-b015-c6b2ad1bfde8",
      "created": 1638101048595,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006872",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "35461224-210c-4062-b7f8-31e96ad5d4cf",
      "created": 1638086673420,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007118",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "2062267b-9740-41a9-b95d-45b94614913d",
      "created": 1638072206428,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007145",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "e7dff5a2-df53-4be5-82b8-baf1e551d3ad",
      "created": 1638057800523,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007092",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "d9878eb5-6267-471f-b56b-cd11cf33bf58",
      "created": 1638043418658,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007288",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "895ff37c-4d51-41c1-9b10-963ebe005337",
      "created": 1638029059024,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006956",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "85c8ee7d-f469-453d-a35d-8b4c5f81a2f8",
      "created": 1638014667774,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007195",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "858e9619-82a9-4a86-9e6a-f11702b094f1",
      "created": 1638000334635,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007484",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "c85c5aa1-f6a4-4cd1-84a1-3c9adfab3d1c",
      "created": 1637985921889,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008033",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "af010aa5-3843-401d-97ad-91dd6068627d",
      "created": 1637971411510,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006437",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "af6a65f7-5675-4d59-86ed-bf2ebb00410e",
      "created": 1637957091539,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006095",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000122
    },
    {
      "id": "ae2f9806-5b75-4ad9-a45f-ec502570e369",
      "created": 1637942696273,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006760",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "9a45f30c-51f8-4790-8929-6a4e887323e0",
      "created": 1637928257603,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007753",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "1f4e8435-d742-4273-af74-0bb29f85521a",
      "created": 1637913870738,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006608",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "d2b56263-df93-4bbb-9bed-7f1702e216d9",
      "created": 1637899467467,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007017",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "0b7214cd-2ea4-4a08-9c4f-cb2cd6492519",
      "created": 1637885070738,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005822",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000116
    },
    {
      "id": "62c01c46-6278-44a8-b076-9360842edb1f",
      "created": 1637870615416,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005425",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000109
    },
    {
      "id": "da95f37d-1ba3-480a-9049-9ab52b358114",
      "created": 1637856201680,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005317",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "903cdb41-f91a-4644-a864-11ea92557f2f",
      "created": 1637841904305,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005460",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000109
    },
    {
      "id": "fffe896b-a768-418f-969f-856daede2423",
      "created": 1637827481123,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005349",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000107
    },
    {
      "id": "42a476b2-633e-403d-b1a6-9bcf87e94bd3",
      "created": 1637812994574,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007296",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "dd83c000-8fd1-4d6c-8bd5-ba286d3fb34f",
      "created": 1637798614985,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007097",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "7bbafc9a-e854-4042-85b0-96fa9b200781",
      "created": 1637784278842,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007360",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "b4bd0dfd-7b23-48f1-8e2e-1bcaa614ca59",
      "created": 1637769807779,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007421",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "ee1d40dd-1c65-438d-83cc-1a498e9607d5",
      "created": 1637755400395,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007060",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "47260938-8ffd-4f80-9570-3b970bb7ca74",
      "created": 1637741073176,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007150",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "44dc251e-f02c-43d7-9ef3-924a982987d9",
      "created": 1637726694835,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007091",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "f3dd4a2b-32b8-45bc-914a-911dc7c5bd03",
      "created": 1637712343546,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007110",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "fcba79e1-d367-4521-8f0d-e3d32eeaab51",
      "created": 1637697826050,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007185",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "8f248a61-1c2c-4c4d-976c-ed707ecaac69",
      "created": 1637683423128,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006349",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000127
    },
    {
      "id": "cdaabd30-41b9-4510-894a-ddada818494f",
      "created": 1637669295903,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006382",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000128
    },
    {
      "id": "81da0ba0-4f6a-464b-af6b-61dd128b644a",
      "created": 1637654635167,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007257",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "944bfa6c-89ed-4d2d-96a5-1603dad73fdd",
      "created": 1637640371582,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006891",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "00463b23-86da-44f7-b01b-bc090365edc7",
      "created": 1637625827646,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007013",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "8ebd32a3-f4aa-426f-98a7-1ff259ae6529",
      "created": 1637611432612,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006806",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "fb7b85f0-3a14-4075-b1be-70526dac8cc1",
      "created": 1637597185834,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007207",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "a59360ce-7508-4282-87ff-2c527ab32fba",
      "created": 1637582637899,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006972",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "7a8ce9ff-ff2f-4e4f-9e63-1c831cf63edb",
      "created": 1637568305045,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006927",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "3404800f-483d-4f68-8010-822fc6eef28f",
      "created": 1637553870722,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007024",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "32426f3c-2d1b-4423-81c9-509425cf94e4",
      "created": 1637539683884,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007051",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "5d53d831-2471-4217-8b45-d16f75fb9ea1",
      "created": 1637525079202,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007003",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "fe856b75-ebd1-4a3f-ac6b-8232036af6f7",
      "created": 1637510690297,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007008",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "7f68aafd-347b-4bfb-a740-bb6a902dd907",
      "created": 1637496548263,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007487",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "f66ad7a3-798d-4f59-b346-1828fac573b4",
      "created": 1637481906186,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007289",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "a5b32f47-31a4-41a0-a5cc-2d4e7ffdfad1",
      "created": 1637467420667,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007141",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "bd6a6584-92f5-422c-8e24-fe018a6589aa",
      "created": 1637452998618,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006975",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "c1311abd-8c08-414f-a36c-7a865f3806f5",
      "created": 1637438709248,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006944",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "32e51f50-c80a-43d7-9222-821ec6b330e4",
      "created": 1637424258938,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007296",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "33c9dc9a-fe9e-4807-95ee-69bc534d8d95",
      "created": 1637409858323,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006833",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "a183daec-c0ee-47ba-910e-1ea624994a11",
      "created": 1637395546580,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006996",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "63eb1075-a55d-496a-8ff3-766847c23fbf",
      "created": 1637381116567,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006944",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "e71bf2ee-5ef2-4b5b-bb24-af87aa0d3941",
      "created": 1637366606244,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007201",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "53c55c9b-5154-43d1-80b0-842b4e932b5b",
      "created": 1637352377134,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007337",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "5e7eafad-e1a0-4dd5-a972-0f9224c5f536",
      "created": 1637337817160,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007155",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "fe3215fa-3e7e-4859-8ffb-2f0f24c0a6e9",
      "created": 1637323458275,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006839",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "ec69cd31-5602-4f66-8057-0d29d62d129c",
      "created": 1637309170430,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006618",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "e93e6182-898b-4967-b80a-a479df6ca2f0",
      "created": 1637294862077,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006508",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "cc120313-1d10-4c53-af43-c1da1a54367d",
      "created": 1637280296667,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006481",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "9c62ca49-740c-4a13-a5bd-ef18f3137459",
      "created": 1637265934868,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006181",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000124
    },
    {
      "id": "83926658-eac1-4424-8be5-30e070889eb6",
      "created": 1637251560419,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006749",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "da0ab955-b75b-41e5-93ee-24b357b357e4",
      "created": 1637237285510,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006639",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "dba7e414-1e9f-4b06-a0d5-660649bb6268",
      "created": 1637222726581,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006972",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "c0ebd224-deed-4ef9-b911-911958d71b02",
      "created": 1637208226313,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006708",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "ebd34d11-2dc3-464b-9199-73e8725025dd",
      "created": 1637193915364,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006912",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "2bb89ddd-5f1e-4b2a-bfee-47757454ea19",
      "created": 1637179441290,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006742",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "c7825dcb-fad8-4315-9e09-ecf10b17f555",
      "created": 1637165157898,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006572",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000131
    },
    {
      "id": "f961e9e5-8f4a-4e62-8c98-336847227640",
      "created": 1637150669402,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006847",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "459d02c2-d787-450a-9593-f678a64180f1",
      "created": 1637136307316,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006615",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "781ead0f-d602-482e-bf82-89d38dd091b6",
      "created": 1637121796766,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006947",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "5f3d05c2-8829-4dda-a15d-2008b19ea5ee",
      "created": 1637107487500,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007119",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "bfee0ec2-9972-487d-a002-6b1fbfd20d40",
      "created": 1637093109700,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006909",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "e5fa29f2-a6f4-4b3e-8be6-19a31689e57f",
      "created": 1637078683170,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007040",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "52248582-48a9-4681-ae5d-bc28bc496197",
      "created": 1637064470867,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007032",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "03a0edb0-2ed1-4cc4-94b8-71af47c9cb7b",
      "created": 1637049990644,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "9167be51-03ae-4b3f-b92d-a82b2a210d85",
      "created": 1637035379106,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006899",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "722635f3-6bed-4837-ace4-33903f84b65e",
      "created": 1637021120083,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007304",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "ec1d446f-a8d1-4c9b-815a-6fa57206ef20",
      "created": 1637006673962,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006999",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "41164e8b-f57d-42cf-ae8b-ac8f8ec99937",
      "created": 1636992397595,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007089",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "7e71fe8e-1351-45ed-8966-cd01a61cbbe5",
      "created": 1636977947660,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007047",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "ece7982f-f9ae-4d5a-8e59-1fc25936ff2f",
      "created": 1636963427270,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006913",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "aa0279ad-83d6-42d4-8cdc-590bece9dfea",
      "created": 1636949111993,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006727",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "f6392f3b-2a4a-4b0d-90d9-e5faccb03fe7",
      "created": 1636934678732,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006731",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "bd08d7e0-8bdc-4e35-8f3f-26575485fcab",
      "created": 1636920195612,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006886",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "b85750d5-8aa9-4f73-bc20-09612a750029",
      "created": 1636905865250,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006741",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "508d6cb7-5dcb-4283-91e5-4b9cf5b60530",
      "created": 1636891478440,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006888",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "4e7bcac2-09ed-4b53-b3ad-b4a28aa04411",
      "created": 1636877174380,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006778",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "e190ac7e-5baa-4311-b7f4-f5947f014d0c",
      "created": 1636862670131,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006866",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "7a6dcced-9504-4a60-8a8a-9019eef93300",
      "created": 1636848286732,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006809",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "a338f75a-874d-4b21-84ef-809d2b302e11",
      "created": 1636833831388,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006971",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "2a8a850b-49bd-40d7-9170-a4659a74637c",
      "created": 1636819532654,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006932",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "529699c8-de88-4a4c-860d-ef81d7261fa8",
      "created": 1636805050847,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006979",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "9d532276-4312-4132-879d-624d9b2a36ee",
      "created": 1636790707066,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007023",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "1028836f-36fd-49bf-ba98-9ae58a479c25",
      "created": 1636776382372,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "391c370b-5c2a-4613-ba4f-ea4d01c4d2d0",
      "created": 1636761833632,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007180",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "bd246852-e3c0-4fb2-8fd8-d11109e61092",
      "created": 1636747695429,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007026",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "d4820b88-3102-40c7-b2dc-6afd8e287794",
      "created": 1636733022275,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007090",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "6032cf48-c374-4c26-a2e2-a5563bb4b981",
      "created": 1636718781193,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006487",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "a6b5d058-70da-49e0-bf47-755f80267f41",
      "created": 1636704240406,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006432",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "81bf36da-b3cf-4e16-aa13-aae43ec2eeee",
      "created": 1636689851312,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007041",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "af90f424-b646-420a-9bde-14f5d07594fd",
      "created": 1636675436913,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007360",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "b6fbdca5-c6ca-482e-9a92-2b079d1222ee",
      "created": 1636661072146,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007192",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "34dc2fe4-27a8-4b9f-afe8-8d4031619b87",
      "created": 1636646705686,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006456",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "f86203da-d503-4a5f-9405-dd281ccc2e23",
      "created": 1636632318787,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006641",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "e96325a3-df21-4a2d-a729-5dbefde3c0d3",
      "created": 1636617935302,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006088",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000122
    },
    {
      "id": "148a52ca-807c-4400-86f6-74634977a3ef",
      "created": 1636603471368,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006975",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "e9d92f8a-114b-40f5-8b06-a420e4db7c16",
      "created": 1636589035713,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007359",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "7de14465-c0e2-4c36-88d8-82f2a8141ea3",
      "created": 1636574759779,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007162",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "aa6ec2da-7c51-4b28-a045-7804f9db4dbb",
      "created": 1636560296410,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007343",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "e00a0e30-0c43-4b13-85b4-2fdebd25670e",
      "created": 1636545961252,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007298",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "5be3472f-2f2d-4503-829e-9ea8132d818e",
      "created": 1636531663377,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007428",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "0f7e373a-4066-4a5f-91fe-bf4e30437878",
      "created": 1636517029889,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007316",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "68782efa-b86f-4e1a-9247-33a856bb0eee",
      "created": 1636502659412,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006818",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "81844eab-b685-4ba1-a125-9019f54c7330",
      "created": 1636488264012,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007510",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "fcc1272a-f893-4c24-ab77-7351db919744",
      "created": 1636473814541,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007427",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "f77c07a1-2123-4dce-b612-ee4d65f6309f",
      "created": 1636459489714,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006921",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "4fcf1d36-a0dc-4533-a20d-eef6dc6bf09d",
      "created": 1636445041094,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002582",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 5.2e-7
    },
    {
      "id": "267d6709-19a4-415d-b69d-fbbf78ff337d",
      "created": 1636430666611,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001839",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.7e-7
    },
    {
      "id": "e8132c57-404b-4810-85de-379cd196922d",
      "created": 1636416315768,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001857",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.7e-7
    },
    {
      "id": "9318609d-e4c0-4578-90db-4c3f4206ffb1",
      "created": 1636402058317,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002034",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.1e-7
    },
    {
      "id": "91072dc5-c203-4086-bd4b-469d83217e2b",
      "created": 1636387680674,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001877",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "49bc9dc6-67da-46ec-b253-e2bd29fcf121",
      "created": 1636373165663,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001846",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.7e-7
    },
    {
      "id": "3b1c6056-cecc-4172-a161-4fef072b7e92",
      "created": 1636358750656,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001922",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "2f4b1451-ae70-44a6-be70-9cf765ad8017",
      "created": 1636344244508,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001854",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.7e-7
    },
    {
      "id": "cf22ddad-c3ad-4cdc-b521-cf41dee1c4fe",
      "created": 1636329784133,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001882",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "e739b1fd-bdb3-4cb0-a719-c69408d25a6b",
      "created": 1636315450623,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001963",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "4d6b8f24-0c66-4e6a-9a3e-9248c100b23c",
      "created": 1636301024612,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001929",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "c53ddb06-ba36-4307-807d-e6da31447e92",
      "created": 1636286674549,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001972",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "435baebd-9411-45c6-9181-54bd026a0347",
      "created": 1636272191013,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001926",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "5f498dfc-b8d6-4b97-9695-3beafffd39cc",
      "created": 1636257848195,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001979",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "0edef0e4-c8f7-497a-a7a0-0f34e5fbfbdc",
      "created": 1636243378947,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001971",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "0d26aec4-12a4-45b8-8ca2-1cbc4cf01e06",
      "created": 1636229010735,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001900",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "3439e967-eb81-4ef4-8d59-95a7dd5f23fb",
      "created": 1636214677650,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001933",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "e08a4142-486d-4030-90b3-794903ab1875",
      "created": 1636200287188,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001981",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "10582a71-a25d-4575-8b65-407140245f44",
      "created": 1636185796496,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001779",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.6e-7
    },
    {
      "id": "292120b0-09ab-4304-b040-2f85a583d53c",
      "created": 1636171487127,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001888",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "95373dde-dd1d-41a9-b90d-cddf9f99eea0",
      "created": 1636157019688,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001967",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "262ebf51-1c38-442a-8e79-8b14793f2699",
      "created": 1636142669487,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002013",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "4ce69728-d4e2-40fd-a017-2a01d4d197a7",
      "created": 1636128254513,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002070",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.1e-7
    },
    {
      "id": "cf623a62-4991-4265-a074-e36dda4740b9",
      "created": 1636113856797,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001931",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "df7a6110-4f2c-46e2-8360-f3c4e73c7f3f",
      "created": 1636099407895,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002044",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.1e-7
    },
    {
      "id": "378c3d5e-02fd-49f9-b61f-ac7f7eed163f",
      "created": 1636085115243,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002004",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "68b1c638-d8ee-4125-baec-a959546822dc",
      "created": 1636070648651,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002308",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.6e-7
    },
    {
      "id": "ebf191cb-f85b-471f-8952-df62fc795586",
      "created": 1636056324109,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004302",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.6e-7
    },
    {
      "id": "9ffd9635-ec98-472c-8bb5-6c276bdcabf3",
      "created": 1636041832810,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004448",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.9e-7
    },
    {
      "id": "8a5e00da-ec9f-4553-a49f-6309b5d2ae85",
      "created": 1636027809494,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004488",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9e-7
    },
    {
      "id": "13b34b16-4518-4a76-8041-406e0df9bdeb",
      "created": 1636013289936,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005213",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000104
    },
    {
      "id": "0e436cc0-2cdc-40a4-abcf-4683abcc6e69",
      "created": 1635998708747,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007207",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "5bf0cc2d-13b1-4b39-b504-6c402d794531",
      "created": 1635984226904,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007330",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "72d1da34-67cf-49ec-82a5-f881693a7f83",
      "created": 1635970004940,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007865",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "8d7acecf-a9c2-4a2f-abee-7a483d6934e6",
      "created": 1635955546542,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007337",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "af3ef7ca-0676-4e6a-8ab0-136aac976e19",
      "created": 1635941132297,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007252",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "d0da499e-5e9a-40f5-ac82-820106ca7539",
      "created": 1635926689768,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007331",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "eba877d9-6902-407d-983c-94b282725ab7",
      "created": 1635912308998,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007391",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "762bb79c-5acd-43ca-b742-401907575474",
      "created": 1635897825423,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007750",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "71ea640d-cde0-4460-adc1-1e7bc06e9891",
      "created": 1635883404812,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007444",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "5636fe6d-54aa-4bbe-81f6-d99f7131005f",
      "created": 1635869015506,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007208",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "5ffdd6f1-0188-4cc8-b248-9dfdd615b07e",
      "created": 1635854591028,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007187",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "e3ba0266-6051-45db-9a03-adf723dcdfb9",
      "created": 1635840315836,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007075",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "003d1852-49b1-4287-ae0a-82b671ea5a83",
      "created": 1635825881820,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007207",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "9686a3ab-01fc-4795-8e8f-17757381d145",
      "created": 1635811395051,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007430",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "d2678712-cc33-4668-8296-2142fa3b19a3",
      "created": 1635797104377,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007841",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "c5f6d5b6-6482-47cd-9239-d349d35b075e",
      "created": 1635782612165,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007432",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "b43c55a0-75f5-422d-8d76-93db332b8b5d",
      "created": 1635768204532,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007110",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "460fefbe-bbb5-4b36-a327-00c06b317a25",
      "created": 1635753847115,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006933",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "cc5ff3f0-4730-4d19-85b3-62d3a6cb22d4",
      "created": 1635739482167,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007420",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "6ca5ef88-d113-490c-9d43-6a52d22afdc4",
      "created": 1635724995935,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007476",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "c7021aea-56fc-4218-8f43-2fc0013a8141",
      "created": 1635710671117,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007587",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "659c2c79-2e31-4e51-bd15-0f2aa54e86e8",
      "created": 1635696246194,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007526",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "91ee8c6d-0397-4d10-8e64-5371afc46bdb",
      "created": 1635681884033,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007374",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "146f8d4a-d201-483f-afbd-c1838081649d",
      "created": 1635667452163,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007550",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "12d42f1d-06ff-4aab-b8f0-70dca6b8833f",
      "created": 1635653068222,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007404",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "c1c3a169-6422-4b63-aa8e-9057a21a554b",
      "created": 1635638609047,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007623",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "1c6f0d30-00a2-46f2-bac2-4a9bdcc1ec6a",
      "created": 1635624195407,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007675",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "ca2ea033-8ca7-4434-9816-9b8038fbb6b4",
      "created": 1635609799631,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007502",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "10c49d89-6145-4d95-92f1-3273d387aa80",
      "created": 1635595403879,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007351",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "44495364-118c-48de-962b-28944c3a3e9c",
      "created": 1635581059977,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007351",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "b70b532f-1dc4-4750-b4b0-cfda11856493",
      "created": 1635566651529,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "ece37147-62f2-4816-b33d-af25a86eb965",
      "created": 1635552239277,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007502",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "2482b4a5-7571-477f-9f59-89b36714c963",
      "created": 1635537884230,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008102",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "6855d5ba-405b-472a-966f-11df48fd3c5c",
      "created": 1635523449452,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008076",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "2758bd42-93d1-4e9d-a3f7-ccc804b351f2",
      "created": 1635509075387,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007625",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "385e93e0-e7a0-4f6e-be55-c7bd856edab8",
      "created": 1635494689809,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "604062a7-8f50-4cf1-818b-f09f52f321f9",
      "created": 1635480268742,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007364",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "96fb3d8b-c5e7-49e4-987e-9afe42ebd04a",
      "created": 1635465790572,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007486",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "c94197f4-af88-4702-83aa-c3f91f68988c",
      "created": 1635451502597,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007867",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "85ca19e2-4fa5-4565-a7ac-be82bf99a952",
      "created": 1635437094445,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006523",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "a4cece0e-4c1d-47ab-893e-1edf418a49cf",
      "created": 1635422779258,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001927",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "bf13a02d-5040-4559-a2a9-c8dc49d1ce45",
      "created": 1635408543534,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002002",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "753ac6bd-ca5b-48fa-af93-b5a20463f322",
      "created": 1635394045578,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001997",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "8ce31b43-5a23-4372-a704-405743491a1f",
      "created": 1635379518872,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001997",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "842bcd87-1101-4e73-a6b8-07c23f89df46",
      "created": 1635365160041,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002012",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "7a973819-9909-465b-b2d4-7a181373c729",
      "created": 1635350594307,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001971",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "af991fb3-43d5-4ce3-98d6-fe9029c98783",
      "created": 1635336304326,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002027",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.1e-7
    },
    {
      "id": "77af1cea-cee8-4288-931b-eb06fb36a0af",
      "created": 1635321841920,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001947",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "d0445b65-eaad-4f7a-ba33-54fb00ee5371",
      "created": 1635307435240,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001902",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "4dc110fb-d7db-4778-adb7-3ec851e6708c",
      "created": 1635293011189,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003997",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8e-7
    },
    {
      "id": "655b0112-0bf8-4de3-a1ea-a6825e21fca6",
      "created": 1635278642321,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004153",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.3e-7
    },
    {
      "id": "8e7e28cb-843a-45e5-88c9-939447180900",
      "created": 1635264215819,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004010",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8e-7
    },
    {
      "id": "795b6f50-f6ab-4061-b59c-20f8091f1975",
      "created": 1635249863148,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004004",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8e-7
    },
    {
      "id": "c7de8c8a-5b7c-4cfe-8d2b-4a72f16c894c",
      "created": 1635235424268,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003850",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.7e-7
    },
    {
      "id": "e2d99cf0-f9bd-485e-8651-5a23f80348a2",
      "created": 1635221047740,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003941",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.9e-7
    },
    {
      "id": "767bba07-fcc4-4cb2-9194-d6cbee579851",
      "created": 1635206693045,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003990",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8e-7
    },
    {
      "id": "b7de9cee-c409-4d28-b17e-df1b885e8587",
      "created": 1635192266755,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004060",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.1e-7
    },
    {
      "id": "a67732b0-cea6-4745-a75a-18831e4f37ee",
      "created": 1635177807559,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003785",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.6e-7
    },
    {
      "id": "68052d5b-0373-4d7a-9ca1-326d3b8e70d1",
      "created": 1635163449829,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003719",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.4e-7
    },
    {
      "id": "c033e480-b2a1-4cf7-9963-f9c43aacd5dc",
      "created": 1635149098205,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003986",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8e-7
    },
    {
      "id": "81e5c430-3937-49e7-9acb-78cc0dad31cd",
      "created": 1635134631605,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004136",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.3e-7
    },
    {
      "id": "30db9830-ebb4-45e9-b1d2-c59eb13c0f40",
      "created": 1635120177877,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004147",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.3e-7
    },
    {
      "id": "c0eb299a-569f-4a67-87d9-8f3e2c7faff9",
      "created": 1635105829064,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004003",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8e-7
    },
    {
      "id": "3588ce14-988f-4334-a40d-5e4b70913dab",
      "created": 1635091435447,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003933",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.9e-7
    },
    {
      "id": "c7b26724-7964-43f0-8757-793c16af7247",
      "created": 1635077062099,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003896",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.8e-7
    },
    {
      "id": "1ca89182-3dbf-4a59-a7a3-31a1db52cb2a",
      "created": 1635062696430,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004007",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8e-7
    },
    {
      "id": "9088d9f4-9564-4b11-a850-c469ae1ae67a",
      "created": 1635048237744,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006768",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "6efec1df-4c16-4d65-9449-fb1979af3343",
      "created": 1635033817457,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006921",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "834cceed-4f58-426a-b79d-fc0debf5424d",
      "created": 1635019446850,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007270",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "fae96d81-dfe9-4af5-90be-b675b50b5e47",
      "created": 1635005028454,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007008",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "7d5ebab9-2c00-48a9-a5a5-1cf79d5a21d7",
      "created": 1634990626762,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007293",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "db1d7c07-6445-45cf-b9c9-33d8fc3a9cb7",
      "created": 1634976217347,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006933",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "57460b70-2b9f-46ed-90bb-124403649d20",
      "created": 1634961832334,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006540",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000131
    },
    {
      "id": "2606d16d-5cca-4c52-90e3-4dc8c98be1e1",
      "created": 1634947529152,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007009",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "16b2e468-0a8a-461c-b86a-440042b2c6eb",
      "created": 1634933041576,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006988",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "5864fca5-a944-43eb-b6e0-66104a7fe86d",
      "created": 1634918692624,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006859",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "a931f6cc-a8aa-49f2-aacd-213047505c2c",
      "created": 1634904281355,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "8f1ccc37-a4a2-4a9f-a2b8-8667d7d2d606",
      "created": 1634889803479,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006913",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "894c8525-d582-470a-80bd-c6dc177cd779",
      "created": 1634875438443,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006819",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "c8603266-c840-44a2-a61b-c34d429fedad",
      "created": 1634860989645,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007047",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "2da26be7-4ed8-4845-b094-7f256316661d",
      "created": 1634846633333,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007712",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "dccf7ee4-bfb2-4a4d-88cf-5224dc3dec10",
      "created": 1634832201775,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007165",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "6708c017-1165-4537-a700-fc031e30d922",
      "created": 1634817817190,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006986",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "5d0b34b9-dee2-418d-a122-450727720592",
      "created": 1634803426749,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006819",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "36e1fc09-3370-4d6b-81b3-6f9188f8b523",
      "created": 1634789091675,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007145",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "6dff4596-5af6-423d-99ff-69cba7b55d43",
      "created": 1634774672849,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006858",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "0c38d47c-6de4-439d-b9e3-ec8d635f67d2",
      "created": 1634760226948,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006887",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "5deb39b7-a5cf-45ca-b2de-d740b96fb848",
      "created": 1634745943034,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006514",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "8d993cf5-b8a5-4086-9f46-94a8bf6f7a41",
      "created": 1634731656826,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006583",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000132
    },
    {
      "id": "cc5e8367-a821-4548-9526-a79f0514fb90",
      "created": 1634717090081,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006260",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000125
    },
    {
      "id": "762467b8-c292-471d-a490-f3d106746a0b",
      "created": 1634702586185,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006292",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000126
    },
    {
      "id": "c1bd4d38-7539-484c-996d-b467be0a7207",
      "created": 1634688253741,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007005",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "b440567c-5bd0-4e4e-89ea-117c86f8800e",
      "created": 1634673857922,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006828",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "5afe3f8a-929d-42cc-99d2-2d69fae22216",
      "created": 1634659544112,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006687",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "a6cea634-a887-43c7-8601-2f6f58fda09e",
      "created": 1634645062240,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006875",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "7ccb3a64-ed34-4682-9a94-c0bdd5ec1888",
      "created": 1634630581446,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006964",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "7f6e404e-8922-4ff0-b1f7-7a5d28faa05c",
      "created": 1634616189193,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006882",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "5fcc15ff-a057-466b-94f8-3b1aac58c674",
      "created": 1634601871973,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007107",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "9ad0a87d-7399-4f74-ad84-929bc0af1f51",
      "created": 1634587504104,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006741",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "1a466257-6003-4b4f-a799-e1a78ed29d66",
      "created": 1634572996638,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007043",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "b958cf93-99e3-4ae3-99a6-cfe8713e56d7",
      "created": 1634558636648,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006824",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "8ed485e8-7cb8-4bb1-8817-79f25f332cb2",
      "created": 1634544186719,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006943",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "3dd5fac9-356b-495e-9d7a-60efbdefd5fe",
      "created": 1634529802627,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007141",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "ab615de2-ae0d-450c-96a0-7b7012395ebf",
      "created": 1634515370813,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006779",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "397594f9-e97a-428b-bcc2-fa6862fb852d",
      "created": 1634500998006,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006853",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "0eb39014-3000-4a1e-9970-68a4726b8a81",
      "created": 1634486587104,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007052",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "778f823b-f94d-4272-b0fe-cd9a0667d8a5",
      "created": 1634472217620,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006874",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "c37a34d1-7fff-41cb-8487-f605883b7b1a",
      "created": 1634457781062,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006997",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "4bf3adea-5827-4249-bbd5-2944b129670a",
      "created": 1634443395285,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006754",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "b28d4e39-4e1f-4a06-a25a-787da872b896",
      "created": 1634428972838,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006716",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "cc236d49-b458-4b3f-b975-50a17e8d3555",
      "created": 1634414571169,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007333",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "325d1776-965e-4598-8950-78098596de6b",
      "created": 1634400176734,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007307",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "51bea3b2-8ecd-46b7-aeb8-87e4896b8327",
      "created": 1634385872297,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006963",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "2db5b93a-8d6e-42df-95df-af6ee2b2c7bb",
      "created": 1634371393213,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006938",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "a5e2b03e-fb74-40ed-a0ee-86fc3ba6ea84",
      "created": 1634357052784,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007345",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "bf2742bb-aee7-4038-a719-c343cdceb628",
      "created": 1634342650458,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007556",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "745f6dea-e23e-4456-b75d-306537c1e6ce",
      "created": 1634328358598,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007262",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "96ddbf8f-56ea-41eb-b25f-eda7626a1cd4",
      "created": 1634313783607,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006437",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "2582e6d1-e1c6-40f8-a87d-6b6339eb16c3",
      "created": 1634299399159,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006829",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "dafd6263-9a45-42b9-bed3-351832ac2e0a",
      "created": 1634284988032,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006857",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "76da2996-dd08-4874-bf22-8123a07074bf",
      "created": 1634270608827,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007224",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "eab797b1-c3f8-452e-b1b6-94dbf8992195",
      "created": 1634256168621,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007384",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "aee9d725-4b2f-43ca-a1bd-50b8c3483ac3",
      "created": 1634241878964,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007298",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "89116c76-985a-4ab0-9ce7-8e860e370075",
      "created": 1634227386857,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007314",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "3bc4ae08-8e39-4fe2-ac93-e71bda09933f",
      "created": 1634213036284,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006735",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "30339feb-562d-4ac8-9b19-d02c2f43db5c",
      "created": 1634198584923,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007161",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "4715a8ad-2621-4153-9268-8576746afe1d",
      "created": 1634184204656,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006887",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "4db84c8b-0888-4a8e-8e85-25fb23c93e4c",
      "created": 1634169854000,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006807",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "89545b0f-9b0f-43a8-b87b-8538f08d2304",
      "created": 1634155404325,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007082",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "10719670-6941-4965-8ca1-bbed802da612",
      "created": 1634140970548,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006906",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "8664c4ea-d382-473b-ad69-7d98710760dc",
      "created": 1634126706995,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006566",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000131
    },
    {
      "id": "d97d3ea0-bcea-4222-81a1-a2e073d56fbe",
      "created": 1634112325836,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006477",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "3c70f5cb-8ddb-4ef8-b4e9-410c924486ae",
      "created": 1634097954186,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006500",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000013
    },
    {
      "id": "709020c0-cd9e-42f7-a75d-b28a1e78887d",
      "created": 1634083537541,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006385",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000128
    },
    {
      "id": "05a80d5c-206f-4966-9b4b-d34e3d560f73",
      "created": 1634069109434,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006298",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000126
    },
    {
      "id": "e9b57025-6ec8-4405-af02-6bdad33edd39",
      "created": 1634054692840,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006461",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000129
    },
    {
      "id": "5cc90a86-e3e5-42e1-b192-8305560c95a1",
      "created": 1634040177893,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006702",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "62056c8e-5128-4457-9d0d-ada216a5eca2",
      "created": 1634025803137,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007030",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "7de9b953-0251-4b06-a6f2-66895ddb3bdc",
      "created": 1634011365940,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006782",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "8b1d3c8d-e7b3-4db4-b87b-608f36d64aee",
      "created": 1633996981030,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007025",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "428a96ea-67b8-4efe-93bb-5c19b7592d55",
      "created": 1633982670371,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007028",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "17b0208a-aeb2-4512-b63a-fee1c50b526c",
      "created": 1633968135942,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006999",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "63a769a4-31d6-4106-9ec2-65edf5a9abc0",
      "created": 1633953723197,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007171",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "2a3f4fd2-9e64-45b9-8a61-ca919d1c2bca",
      "created": 1633939451600,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006942",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "5b36c553-fc93-4a7d-9360-33edbfeefa8d",
      "created": 1633924959307,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006974",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "b5b0a085-d285-4837-ada4-0b919947ed74",
      "created": 1633910517407,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007469",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "1931b714-c250-4c56-bac8-d46ead494bf5",
      "created": 1633896176692,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007135",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "e00af269-ba33-42a3-9fc0-7f82c483afc9",
      "created": 1633881714592,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007234",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "1425474d-c638-4d40-9fe6-f70f6bd5d12e",
      "created": 1633867376351,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007202",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "2b28d847-ad08-4c7f-8326-05b37d48561c",
      "created": 1633852992588,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007264",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "4a0eb7d9-51bf-48d7-b575-0775a8d805da",
      "created": 1633838570522,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007287",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "4b348d85-cfaa-40c9-b1f9-4b46c2d6523c",
      "created": 1633824160946,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007385",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "2c6c481a-05f1-4065-bf63-f0a07fdef9a3",
      "created": 1633809750116,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007293",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "7ca63eb0-bd19-46b4-bf76-191372ca7805",
      "created": 1633795398042,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007537",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "e1067eba-984a-4b1c-85ad-565119474704",
      "created": 1633780985018,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007119",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "83364513-7718-4f64-8410-58973a832c43",
      "created": 1633766486638,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007198",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "dfcf6fe2-a4b4-40e0-9e8d-e5fcf605fe32",
      "created": 1633752105567,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007343",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "2ed2a87d-a946-498d-8734-f79bc88a8120",
      "created": 1633737794627,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007513",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "fb16ac01-7f3c-4b16-8970-94e4173820ee",
      "created": 1633723345998,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007142",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "ebfb9e1d-269f-49ed-a18c-4e89cb8f6077",
      "created": 1633709012603,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007371",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "5cdae3ca-8ee1-41b8-8210-9f3bab6a6615",
      "created": 1633694522269,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005324",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000106
    },
    {
      "id": "712344bc-a143-4d46-b674-84510b3c54ff",
      "created": 1633680194175,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006642",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "ffbfc225-e5b3-43fb-9bf1-7ad6fe1e3534",
      "created": 1633665637949,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007552",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "f9f9cc34-a5fa-4996-a6a1-726f88cfdce2",
      "created": 1633651247384,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008033",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "e653b2c1-7b7b-4b98-a07a-07ab37cad6e1",
      "created": 1633636980460,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008068",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "6b6ec9b6-b740-41d9-99df-6b2702caee6d",
      "created": 1633622522946,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007751",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "88e6064f-dc9f-432e-911d-8d75770a2c24",
      "created": 1633608139841,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007738",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "f93b03e6-54b5-466a-b1f5-f113ad26e93d",
      "created": 1633593683000,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007926",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "c1a9ca95-40b2-4a7e-bc43-77737be2f984",
      "created": 1633579236814,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007436",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "318b1bb2-4a95-4972-aebb-c556a7fc2a6c",
      "created": 1633564905641,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007664",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "12bf5b34-9f67-411c-be7a-b6d95f790b7a",
      "created": 1633550492495,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007916",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "24a291af-c245-464d-911d-0406f0624931",
      "created": 1633536098344,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007881",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "46cc2451-668e-48b7-93f5-9ea1622976cf",
      "created": 1633521643939,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007900",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "b8e8241a-5c99-42f6-a8ac-c92a0f5ea3f1",
      "created": 1633507298515,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008187",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "93ecdc41-b2a5-4e97-8cdf-2b0b4e95b872",
      "created": 1633492848465,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007846",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "a2008de3-6743-4c39-a965-2a9db14e23d8",
      "created": 1633478442931,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007947",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "1591aebc-3f18-4fbd-81cc-4bb6c4a6e62e",
      "created": 1633464070722,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008207",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "9af9d574-2439-46ea-8276-877748919555",
      "created": 1633449664510,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007751",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "6273a035-9917-4e29-b45c-a53881416e97",
      "created": 1633435231917,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007599",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "13e10910-ef15-4e01-aba6-0040530a4d21",
      "created": 1633420867627,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007738",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "0e2eff9e-8462-42f6-aa94-28185f8dafe0",
      "created": 1633406465351,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007949",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "56ac0a69-4883-4e8b-a09c-1307450a9ecd",
      "created": 1633392010319,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008133",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "5697ed2c-0b78-4d8f-a961-91bbc69fe037",
      "created": 1633377744266,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008281",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "f913ac97-3f79-4293-81ec-d2211c9e2638",
      "created": 1633363316010,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008500",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "ed22dc6c-ac3a-458c-8fa6-c7f259042977",
      "created": 1633348985232,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008211",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "baf30052-cf3c-44a0-af87-bb04ef804aa4",
      "created": 1633334730982,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007971",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "6ce2fa8b-2de7-4fa8-9c48-be1d8985813a",
      "created": 1633320135138,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007655",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "fc424be3-de61-436e-ad36-478b6c7293e2",
      "created": 1633305781294,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007956",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "0f4feb73-1ef3-4634-9e4e-b99a51cd5046",
      "created": 1633291322619,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008061",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "24be9c97-25e4-4ec5-a705-1fa8eeae925c",
      "created": 1633276956430,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007970",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "026c0cb3-e6da-4a6e-8e5d-ed04b35e9bd8",
      "created": 1633262671186,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008162",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "2effd8db-b4e5-4045-92d2-7caa0ddba88a",
      "created": 1633248175371,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008081",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "a64e5108-6bc6-47cf-83c7-01bec98c6b62",
      "created": 1633233623100,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007640",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "7da7a172-58b4-46ef-a400-16f354a216d2",
      "created": 1633219379545,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007882",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "1eb9d66f-ff25-48f4-a4a9-9e8ab1f1acfe",
      "created": 1633204920130,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007973",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "e5c806a1-183b-4c62-937c-517d77431084",
      "created": 1633190510536,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007873",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "2ba9b545-3722-4d25-ae56-1a7b8f9dcba0",
      "created": 1633176215768,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007729",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "274afff3-5acf-428d-926f-512fe47b8a26",
      "created": 1633161758284,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007783",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "d5dc7bdf-076c-45a5-89db-b59a7a5ee80d",
      "created": 1633147379584,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008140",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "b4c70a3b-a97a-4780-beed-84da2b1d5a17",
      "created": 1633132964313,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008143",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "0f9971ac-041f-455b-9193-8fb0e1e049d1",
      "created": 1633118587540,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007834",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "e947d635-d49c-49f1-8978-3096b88851e1",
      "created": 1633104243560,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007898",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "3041ce81-282c-4c21-8d3b-a22dff8bbfb9",
      "created": 1633089824668,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008240",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "7129c230-27b6-4051-a402-13e958e41608",
      "created": 1633075414167,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008251",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "373cc6d3-afe8-4fac-8abf-283c970a78b3",
      "created": 1633060942731,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008458",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "75e6e2a6-5e3d-4ff9-b424-37a6a9eceb04",
      "created": 1633046583392,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008304",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "176bdee1-e55e-46bf-bf10-77b9f501261a",
      "created": 1633032194550,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006917",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "e48333dc-972b-4b67-a210-291dfc4bb3ef",
      "created": 1633017748526,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006235",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000125
    },
    {
      "id": "f78f9641-d788-4b66-86f2-6b970279bf27",
      "created": 1633003424496,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005831",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000117
    },
    {
      "id": "ae74be2d-450b-481d-80e3-3d2064047393",
      "created": 1632988984774,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006721",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "eb512094-774a-4af2-996b-c95b027ee143",
      "created": 1632974541778,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008150",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "1e6ecce3-4642-46aa-9a91-c1b07222764b",
      "created": 1632960188593,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008363",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "3016e5a9-21e8-4635-81f8-b937346ca6c1",
      "created": 1632945754728,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008224",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "0c26d839-ce5a-4e4f-bfe7-94466795f681",
      "created": 1632931384132,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008198",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "a1768f89-2827-4518-b03c-9044eaadf439",
      "created": 1632916994662,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008077",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "ea25fb8d-8ba2-4e6f-918e-1fe52fc85845",
      "created": 1632902583627,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007828",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "5435c642-0869-4ceb-a965-727e94447675",
      "created": 1632888208802,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008013",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "e946c550-fa20-49ca-b1f8-bf96de20aa39",
      "created": 1632873848089,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008092",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "d552c25b-99e1-4a2c-ae9e-c8e8b79d2930",
      "created": 1632859439418,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009214",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "626803c5-7566-431c-87f8-074b817ea611",
      "created": 1632844992081,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008287",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "9c5ff6bc-f64e-412a-8011-0688073eea7a",
      "created": 1632830665551,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008036",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "4cb6b905-89ee-4116-8469-2f29aff2e282",
      "created": 1632816177614,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007879",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "3cfd86db-38a7-40a1-836d-af0b652e6b30",
      "created": 1632801784372,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007907",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "ced68e64-7ef9-4037-a67b-8c6f2b223eb7",
      "created": 1632787425445,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008097",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "bcfa6d4d-2492-4cbb-ba02-a5259f39f490",
      "created": 1632773016428,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008534",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "99ce2452-cbc6-43fb-949a-4da2564ab05a",
      "created": 1632758570914,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008511",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "2fc46b34-8bd7-48f1-abbf-d97bbd55a494",
      "created": 1632744226747,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008395",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "20393d2f-4287-4866-9619-e3c0ef36a784",
      "created": 1632729820522,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008161",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "20cec978-1060-4c34-aa9c-bff4df9a00a7",
      "created": 1632715367855,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007918",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "4ba77ebf-6284-4249-b8d0-20853d7cb1b6",
      "created": 1632701014884,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008196",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "ee826547-e21e-41a0-af2c-c5d70cc85c55",
      "created": 1632686553092,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008014",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "f85c1769-ad1b-4c9d-96f0-3dba353c3b8a",
      "created": 1632672182003,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008428",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "917feb9c-33a6-42c6-8f43-70cff54043f2",
      "created": 1632657846779,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008310",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "c9ba5c0f-1dbb-4d1e-bf5f-fee39496146e",
      "created": 1632643395226,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008330",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "1cc730ea-a2ef-4080-8557-030502aee538",
      "created": 1632629027666,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007345",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "890fe2b3-52e1-4059-a84b-9c2267ea2ec3",
      "created": 1632614602913,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007601",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "b6e13acd-5de2-45f7-b085-e1e11e998ef0",
      "created": 1632600179658,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007790",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "651dfbe7-6488-4d08-aa99-45b50f0f2216",
      "created": 1632585768266,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007811",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "cc8841e0-63b7-406f-8dcc-4480c9cb613c",
      "created": 1632571554043,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007838",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "d4724c8b-0b6d-458b-877e-5a10b4e86894",
      "created": 1632556967828,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007928",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "a20d8f04-cf86-44ba-8d9a-ae0f59e9a10c",
      "created": 1632542584338,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007953",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "c34cc312-f4a8-49c1-bc25-b4157d056d16",
      "created": 1632528153518,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007999",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "2cd674e6-7290-4f0a-886e-3d767bc2ab3f",
      "created": 1632513765137,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008204",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "e6467adf-1958-46e8-81b3-df12b70f4a3e",
      "created": 1632499542441,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008065",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "8a6a6e16-9a45-4063-9476-ea53a567e2d9",
      "created": 1632484993034,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007997",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "a2e691aa-e241-45a2-b77d-502729638ce2",
      "created": 1632470557956,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007689",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "6e5ae969-924e-4bde-abc3-5592bdca8e9b",
      "created": 1632456171785,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008259",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "a9b3332c-98ca-4b03-b239-db67a4f62b8c",
      "created": 1632441772970,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008415",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "6aa691f3-0a4d-4204-9d59-04daa9350cd6",
      "created": 1632427354041,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009089",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "88aa31e4-c753-4bc8-b717-104e005e3625",
      "created": 1632412980195,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008134",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "e5d8cc71-b20c-4b92-a70d-543eab013726",
      "created": 1632398573581,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008574",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "d3164e56-1ecd-475a-ba5a-365f633fd815",
      "created": 1632384288955,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008566",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "cd446425-9201-4dd6-a0b8-1960ff076411",
      "created": 1632369718868,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008249",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "500e06c6-6dd1-4e79-97ec-d00f2116f73f",
      "created": 1632355385960,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008256",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "1a9cc2ba-ff7c-4656-8dd7-ca470be86034",
      "created": 1632340981214,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008550",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "7e5e1ae4-69b9-45e6-9f5d-f31ea16c0f03",
      "created": 1632326550130,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008107",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "996397f9-708b-4492-8777-14cc9962550d",
      "created": 1632312140170,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008009",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "4506735a-ff97-46bb-966c-52ba42faed9e",
      "created": 1632297777063,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008114",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "8fd4e7ba-d51a-4c30-a373-732eef4c1fab",
      "created": 1632283387022,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007813",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "ad3f0fb0-d6a1-4009-9862-b08774484678",
      "created": 1632268919191,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008366",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "6598c949-a73f-4c59-95e5-336d162c3a6e",
      "created": 1632254522237,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008156",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "8f06f999-6259-459b-8953-62948e2845e7",
      "created": 1632240238213,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008343",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "50295c5f-2e33-4ceb-ba6b-f95b3136e205",
      "created": 1632225810743,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008060",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "5c6e5f0d-5673-46fa-b4cc-c5a6336e113f",
      "created": 1632211360475,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008365",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "d360d832-c8b1-4c6b-9622-c55e7ca8fc16",
      "created": 1632196958842,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008254",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "fc617156-a450-4b5a-bb98-c697fe624e6c",
      "created": 1632182536938,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008072",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "41c7436e-cfef-4a06-bd0d-079227e78788",
      "created": 1632168209083,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008664",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "cbdfffed-e651-4455-8d1e-7b3660e09617",
      "created": 1632153799303,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008412",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "57fd94e2-6809-4cc8-9821-b2a9260657b5",
      "created": 1632139409867,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008406",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "73077c49-0cf1-4b8a-9f50-ae7651c69b28",
      "created": 1632125172137,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008319",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "1721bf31-3cf1-45c0-857f-78022460b5b1",
      "created": 1632110640554,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008271",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "f34e410b-d33a-41e3-9654-2745e74734df",
      "created": 1632096154997,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008794",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "313689f7-d31b-4a45-a2ba-4e36da80e5b6",
      "created": 1632081761139,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008260",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "a77d936e-84bd-45af-81c8-0ef56322afbe",
      "created": 1632067359164,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008350",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "96d76819-9a11-48e2-a37b-18e31affe6bc",
      "created": 1632053059051,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008243",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "da4eca84-4df2-48bb-81c5-ce5854f6db8b",
      "created": 1632038578024,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008055",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "aa2fb298-303a-4ad4-ac2c-05ff7bdc65c2",
      "created": 1632024265882,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008049",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "531907d0-2f02-42f3-90c0-5e6e60c9a2c3",
      "created": 1632009790975,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008036",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "ae916203-1389-4918-af71-2d7e6ca18144",
      "created": 1631995371863,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008117",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "1008d3cf-4473-4053-8388-83af528068f3",
      "created": 1631981016078,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008285",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "52c39c82-7074-4a94-83e0-b38f09c70eb6",
      "created": 1631966549552,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008626",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "fc6ca037-09ef-44ec-b2b7-ab5fde361f9b",
      "created": 1631952199049,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007862",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000157
    },
    {
      "id": "4b83b03f-6273-4132-9189-79c3effddc96",
      "created": 1631937805073,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007803",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "012bf70d-e0fb-44a7-9449-ad047a108a0a",
      "created": 1631923371748,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008243",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "2c26c1a9-4e9b-427b-a585-42908abd2a83",
      "created": 1631908995922,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008615",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "23d9d111-0802-4f5d-9ddd-01abfb5b7e67",
      "created": 1631894559543,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008866",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "7673861e-8c1b-4a59-98f9-e2a3b31ee364",
      "created": 1631880236575,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008955",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "7d9b219f-5c82-48b7-bb2e-7edbaee59f72",
      "created": 1631865779106,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008894",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "d9ba6584-c39d-42f9-bacf-f3c00e332492",
      "created": 1631851353867,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008712",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "640005b7-9ac3-4564-8207-b3537d1d61b1",
      "created": 1631836946647,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009418",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "3d70c007-92cb-4587-a5fc-1e27a6c99184",
      "created": 1631822544952,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009556",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "5b7ad462-89e0-435e-94bf-76a51331cb06",
      "created": 1631808182736,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009125",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "65f227d5-0610-46e4-803c-03f262a9feb5",
      "created": 1631793902575,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009087",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "e6dedfc5-c152-4fa2-a35c-22bbbe7225bf",
      "created": 1631779383485,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009466",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "fbe276cf-a1e6-4ef6-9c92-69c85d24a488",
      "created": 1631764956675,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008919",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "cec04bc6-7a40-4a9d-b641-760524ca7ade",
      "created": 1631750600543,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008807",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "155aa83b-0232-4863-a9ce-f5445898828d",
      "created": 1631736247201,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008970",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "7dfdfbf2-4659-46d2-9a2e-64b25b5c9737",
      "created": 1631721767608,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008388",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "f1707bec-fa13-4d36-b3b5-f38d256868c6",
      "created": 1631707405043,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008405",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "83886d8a-5e02-420c-8a25-9f7e19284a75",
      "created": 1631692933903,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008523",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "febc42f0-c8ec-41fb-80a8-5cd0725a24b4",
      "created": 1631678583070,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008418",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "6d98cc83-d5eb-46d6-b071-d82c71f7c72a",
      "created": 1631664165714,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008625",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "d376299b-cb82-4a98-8c2e-ab8ea965f1a1",
      "created": 1631649760504,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009262",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "86456015-b319-486a-914c-85bf6af5e4ba",
      "created": 1631635418483,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008378",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "16a6be06-6828-4a71-a4b2-50e3ad0633d6",
      "created": 1631620998843,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008472",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "470b1996-db11-4133-a103-18cc2de82d9a",
      "created": 1631606665831,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008551",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "e7747e53-8ac4-4160-ae1a-09b478fccae9",
      "created": 1631592197217,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008332",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "02de41bf-beab-4720-b3f1-8a17df9f1b07",
      "created": 1631577801649,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009047",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "9d16708e-0cee-4d46-9fc1-f3414a94a03a",
      "created": 1631563405591,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009183",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "2f42fd11-4fa1-44ae-93ab-47126223d24f",
      "created": 1631549032963,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009716",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "97b972d3-ac08-47ea-a817-0471897c4bd0",
      "created": 1631534698423,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008633",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "99ebbbf6-5008-49bb-b3c7-bbb2e33a7b9e",
      "created": 1631520288671,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008726",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "1d74509e-e352-4c2d-948f-2310132e31c9",
      "created": 1631505769480,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008514",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "0eb9246b-ae14-4fe9-a3ec-b44b17fd17ab",
      "created": 1631491415195,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008531",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "0f8f4b19-7041-4493-9896-7aa8359ebb9f",
      "created": 1631477021420,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008602",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "ec59aeac-5d02-4805-b059-a58064d6460f",
      "created": 1631462613946,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008597",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "ffc1589a-2ddc-466f-a1d2-339e4f5c57f2",
      "created": 1631448221426,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008285",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "8cb273e8-9af2-4170-b6d7-aaf6cf4b11e7",
      "created": 1631433906383,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008250",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "5729c886-fc63-41d5-819f-3d54b8a28d34",
      "created": 1631419387531,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008660",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "d5d2a17b-0508-48fe-8585-5ad15b8b9f00",
      "created": 1631404968670,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008329",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "57b345d9-dcab-4c81-8d32-2dbd9aa5d332",
      "created": 1631390611557,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008828",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "a2583d50-ee1c-47eb-ad36-331114815a45",
      "created": 1631376197226,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008623",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "d00ce1f7-9ea5-4024-bdc2-18b684a44be8",
      "created": 1631361800773,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008837",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "de7634e4-0a24-4222-a6b8-462e83b49112",
      "created": 1631347447139,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009098",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "053fb26f-7b8f-4d94-adc9-d0f7b1de3397",
      "created": 1631333114379,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008804",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "e8b171a2-4bf4-43ea-8249-422731a52c9d",
      "created": 1631318596756,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009319",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "d740b03a-37a3-40ff-95c5-2b08982cb305",
      "created": 1631304164503,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008951",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "6e413fc2-4229-4b44-b4ca-25b58439d12e",
      "created": 1631289831235,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009035",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "914dd05b-4af7-46f3-9119-3cd3918219b0",
      "created": 1631275474427,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009327",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "7e23f8c3-a1e8-4daa-8213-d564673e6ddc",
      "created": 1631260974866,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008913",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "c7c05433-7711-4c24-b736-dac13d8f7ad3",
      "created": 1631246656622,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009391",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "57fc4d10-5fdc-49a6-9fc4-1b4ad40b0c4a",
      "created": 1631232179936,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009713",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "783d095b-3135-47d4-984a-84f18df7e7d5",
      "created": 1631217738314,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010070",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "8569288a-f9c2-4298-a3f2-78952b57dbbc",
      "created": 1631203403523,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010165",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000203
    },
    {
      "id": "8c3841cd-9e89-4b68-9b3f-bb8832639579",
      "created": 1631189086238,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009417",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "f2fd674d-5930-4bb4-9cec-145216dbf1e7",
      "created": 1631174659283,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009543",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "145e6142-ae41-4e14-8f98-781c39a56278",
      "created": 1631160200487,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010517",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "e283361b-593a-46d3-97b2-97efdb4bffdd",
      "created": 1631145731685,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009500",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "e25aded0-5c00-4e46-b9df-dd103358c8e3",
      "created": 1631131394571,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010494",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "aad403fd-cb73-47ec-bbac-6a51fc22dbde",
      "created": 1631116966937,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009555",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "ae23e546-2a40-4e1f-930e-345f2efe03c8",
      "created": 1631102729810,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009482",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "184ce4a7-85ad-417c-9e30-2b5a6e46ca93",
      "created": 1631088342209,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009582",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "7143f280-eff1-4024-9ea5-c2dd612ebb07",
      "created": 1631073836672,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009281",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "34e263fc-8b33-4a26-885d-4d224111d7b2",
      "created": 1631059351071,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010108",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "120592ec-0b4b-4f16-ab10-d290a77490c6",
      "created": 1631044973844,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012494",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000025
    },
    {
      "id": "a666b4f3-f23b-4d9a-94ac-e33922dba4c6",
      "created": 1631030673425,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010482",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "2f02d765-f09d-495e-8e4a-f41bfe8762bc",
      "created": 1631016222942,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009153",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "16d8808b-1600-4d62-9f04-ad2098c5beb3",
      "created": 1631001764028,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009378",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "b9f0194b-276a-410f-a08d-f80ec5fc3327",
      "created": 1630987434768,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009396",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "8681feea-c5f9-4110-8ee5-144acda6c794",
      "created": 1630973014403,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009924",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "3d8bd92f-b6fd-476e-bb64-64c70e75bfdf",
      "created": 1630958548325,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009953",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "528c533d-bbdc-4455-9349-970ed02a054c",
      "created": 1630944216930,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005538",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000111
    },
    {
      "id": "5c928136-200b-4b6f-8220-966c6c5364ce",
      "created": 1630929775772,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005260",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000105
    },
    {
      "id": "4b4cd0f0-02e7-4d3f-8ec2-b47842d93072",
      "created": 1630915357805,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005218",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000104
    },
    {
      "id": "e9ac86a4-a155-4315-8e1b-79986e703b31",
      "created": 1630900924636,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006854",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000137
    },
    {
      "id": "ea85243c-4334-47a7-b183-ab84d6605c37",
      "created": 1630886564363,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009848",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "04cb304f-52e6-4edf-bf81-c1e8e9e4b0b9",
      "created": 1630872132315,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010207",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "7386837c-b84b-4568-9cc7-dd654ab85f62",
      "created": 1630857828874,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009878",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "218ac9e1-a750-40fe-b2fa-1b6632323661",
      "created": 1630843361972,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010059",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "8c7247ee-39e4-4cfa-873b-a4daa3a39909",
      "created": 1630829002524,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010010",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "cc49e1dc-9524-4ea2-971f-9ba0c6543340",
      "created": 1630814642508,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009770",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "060cb798-43d4-412f-ae27-7f2a66e30281",
      "created": 1630800158172,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010119",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "e41315f0-4cd4-4ef3-b8bc-8d3e98ad19df",
      "created": 1630785780261,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011104",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000222
    },
    {
      "id": "335f0d3a-c4b5-4e41-bf45-b00b6181709b",
      "created": 1630771374451,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010211",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "3d6b8d71-3eb3-43d2-85fe-e2c7c1463526",
      "created": 1630756996431,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009930",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "ecc29baa-68dc-4591-af9a-b280b59a2952",
      "created": 1630742585705,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009888",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "9039953e-3190-4eb0-b8c8-d628d2c4b90b",
      "created": 1630728131579,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010181",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "faa47247-58ae-4af4-a329-f02097f8d923",
      "created": 1630713785289,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010100",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "e49ccbdb-544a-4031-a252-efb7cabe40a2",
      "created": 1630699444747,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010326",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000207
    },
    {
      "id": "49348bb8-d7f3-4fc1-a19a-8958d3ebf424",
      "created": 1630684944943,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010453",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000209
    },
    {
      "id": "10eb5456-ccd2-4b71-a117-4680c6c9ffcd",
      "created": 1630670528186,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010483",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "eb605373-ee16-4a12-a317-7bac0097622c",
      "created": 1630656209924,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009727",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "80171a43-152b-4d88-aa94-3b242989e2aa",
      "created": 1630641783513,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009258",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "4a3edda7-8e41-429c-a06f-13c6948586b0",
      "created": 1630627407089,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009840",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "2189af11-0f95-4d2a-b9c3-fbce4bb47de4",
      "created": 1630612982265,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010184",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "f50dacc9-2668-4664-be60-d01b78adf56a",
      "created": 1630598613476,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009938",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "b45fd242-657e-412e-84f3-6b1c2bd7e142",
      "created": 1630584167764,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009819",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "bb240052-c2a5-4e57-bfba-feca93c38753",
      "created": 1630569829448,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009372",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "e987dc85-e150-487d-a0a2-ccb646835fc8",
      "created": 1630555321303,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009672",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "57f2dd77-bc37-40ac-9e2c-9e4badeef55b",
      "created": 1630540947850,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010794",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "9942199f-41d5-4129-a8b4-31753f90b955",
      "created": 1630526585849,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010776",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "d9ae2039-6e1b-4803-b998-5c2e143ef43f",
      "created": 1630512246235,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009831",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "b90e6a6a-3e31-4ba8-adcc-449bb2858320",
      "created": 1630497849257,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009600",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "2b38e590-c9b9-437f-ba24-d2b06e018a10",
      "created": 1630483455799,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009353",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "5b56f1a2-1e7d-4e73-a4b3-e0281ac8993c",
      "created": 1630468953496,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009236",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "08a67eef-000d-4d8e-8566-4a430c44cf8c",
      "created": 1630454552310,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009627",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "4b6cd7c4-af62-407a-ba5a-58fc1192192a",
      "created": 1630440138987,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009149",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "499695c0-8b89-4d91-ac78-53107c16a517",
      "created": 1630425806661,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009122",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "75ebe801-6816-4ef3-9422-16ecec7a54d4",
      "created": 1630411428957,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008839",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "07aeb3e6-fabd-4695-b03e-69a78e523bf0",
      "created": 1630396987670,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009541",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "0efb1029-35a7-4990-b678-a38109eee224",
      "created": 1630382515271,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009958",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "a8f80fbb-d24a-44e6-bbbd-4dfaaad9c042",
      "created": 1630368155356,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010207",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "a35484ef-d702-4522-b5a6-f04d260d5f3a",
      "created": 1630353977275,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005576",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000112
    },
    {
      "id": "6e42d154-91cc-4a05-ab5a-8bb8fcde33fb",
      "created": 1630339365589,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005811",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000116
    },
    {
      "id": "d461eae4-2e5a-43b6-97d0-bb0b97d332a4",
      "created": 1630324939349,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008720",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "72a321ec-457f-4303-91d9-dfbcbafb02ec",
      "created": 1630310557013,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008964",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "6b9cf841-f5ba-4454-959d-8dbdf13b7ed3",
      "created": 1630296131755,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008759",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "3e5cf42b-9193-47dd-8798-1f1f317ffce5",
      "created": 1630281771670,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010536",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000211
    },
    {
      "id": "5fef3042-af5c-4fc2-ad58-bba4a130550e",
      "created": 1630267323029,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008068",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "aa9981da-b6d8-43c1-b9ee-6ba1e472fa79",
      "created": 1630252986362,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000012
    },
    {
      "id": "eaf5e8fc-2a56-43e4-b7a1-79d04e589857",
      "created": 1630238576579,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008425",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "183be212-4a0c-4f4a-8935-fae0f93ac78f",
      "created": 1630224140844,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008584",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "53246d24-76e2-4baa-902b-e97f740c541d",
      "created": 1630209794619,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009082",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "07cb5fb5-4288-4961-8b63-fd10fddfdbbf",
      "created": 1630195324165,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010059",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "e5a2e01d-1900-44ba-b6a9-fd90d606a39d",
      "created": 1630180941016,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009224",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "c79417f9-4ae6-452a-8533-85a4a8e081fb",
      "created": 1630166596852,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008550",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "2acb3562-dfe7-49cf-be5f-e34f34dae3ef",
      "created": 1630152121314,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008916",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "b1c1ca4b-8e5f-46bc-968e-692176e9c564",
      "created": 1630137812687,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008762",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "6d0cfd41-a834-4a8e-b6cb-4ba10f2ebc28",
      "created": 1630123398744,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009012",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "99936e5f-544e-4389-ae58-e7264c1d65ca",
      "created": 1630108992915,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008971",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "462181f6-c81d-4df8-b4a4-0c329f70078f",
      "created": 1630094562525,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010856",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000217
    },
    {
      "id": "8889eb48-8314-4558-8100-36d040546f8d",
      "created": 1630080259074,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009487",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "8fb106f5-b295-4f65-ab3d-4a2966404b86",
      "created": 1630065787310,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008674",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "7be89e9f-31ee-4079-a786-3589b4421188",
      "created": 1630051414658,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008681",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "a1aece99-3f1a-45de-abbf-ca28516be813",
      "created": 1630036988379,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008575",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "73b49a83-2517-41a7-97fe-4753478bb3aa",
      "created": 1630022522976,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008838",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "db362fc6-86eb-4c7d-a20b-30776ecec357",
      "created": 1630008192672,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008458",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "9e11028f-8e4f-4a1a-a2ee-72249206bb89",
      "created": 1629993837023,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007406",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000148
    },
    {
      "id": "dc774778-2e09-4a04-8e27-398b86bad102",
      "created": 1629979395644,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009115",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "e50a6f1e-59cd-4299-896f-aacd402a83d0",
      "created": 1629964976854,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008248",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "7bd9347d-80fb-4df4-8587-ea72d686a060",
      "created": 1629950589142,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008409",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "2a4317be-9079-4c9c-9923-a94a26b7dca5",
      "created": 1629936215108,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009882",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "b757fb93-9490-450f-8430-fc0516fa4d1a",
      "created": 1629921774982,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009953",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "eb02c6b8-833e-4aff-9360-14241b984047",
      "created": 1629907332859,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008606",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "b29b3d53-7aaf-4839-959a-e9606539f810",
      "created": 1629892983337,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008696",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "389cdef1-c96e-4070-8143-db38e7232973",
      "created": 1629878544191,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009191",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "93e2f614-58e6-4768-ac44-0b5154ba4b48",
      "created": 1629864214720,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008812",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "dbd0ebfa-b92b-4716-8a98-66d80c490992",
      "created": 1629849736359,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "9d18054f-ce1f-4b4f-8328-0aade812af52",
      "created": 1629835454905,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009320",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "0ac3784a-6d5e-47be-827f-f0ebf1cf38d6",
      "created": 1629820932032,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008930",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "cf1a9835-2e31-4480-9b08-0465795efc62",
      "created": 1629806660821,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009015",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "8285d62c-ac0d-412e-b31f-7a3c40484428",
      "created": 1629792246124,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008779",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "e5674f67-1f26-4db1-bce5-f0173acff7c3",
      "created": 1629777854990,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009461",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "2599fcb6-52b6-4500-8cb1-157f179c9073",
      "created": 1629763352111,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009262",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "c28bf578-28d0-430e-9954-963d527b1cdc",
      "created": 1629748892724,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009997",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "89abd4e0-69e4-4bdd-953e-f770751d1841",
      "created": 1629734595920,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009494",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "ab6ca296-1c85-4ef8-b154-196a82971291",
      "created": 1629720203630,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008937",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "17c01159-33fc-4a45-bf89-38780ad7871f",
      "created": 1629705758526,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008852",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "57d84e0d-4882-4dc1-8c00-82642754e84c",
      "created": 1629691326258,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008341",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "a1146ac3-d520-4fec-b1a9-86e641f1c3b2",
      "created": 1629676932352,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008502",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "e5a65af2-a164-43c8-a5f3-ad4b35fd55d6",
      "created": 1629662515348,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008885",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "b29a504c-c853-4198-978b-750c358d84f5",
      "created": 1629648254090,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008538",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "992380b3-cddc-4a91-88e3-9fc213e4de39",
      "created": 1629633770904,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008870",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "d8ee5197-a024-404f-ad80-6833bc8c9e4f",
      "created": 1629619427999,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009055",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "b2aaaf32-1b6b-4ce6-bec5-26af2af0faca",
      "created": 1629604930591,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008748",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "0ae438bf-0e72-46a6-9ff8-108d03c54583",
      "created": 1629590516973,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009066",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "4f62a52f-16b0-4142-a066-b53e96923f38",
      "created": 1629576133000,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008739",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "634dd961-fabf-499e-8f9b-e1a75b35dbdc",
      "created": 1629561724420,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008686",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "b29a2314-f99a-47f2-8362-684357d43188",
      "created": 1629547421028,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008870",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "472af337-46a4-442d-9eb6-692df8bdd0ef",
      "created": 1629532966027,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008689",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "0b359d69-00fe-42f0-80ee-a4fa179bd39f",
      "created": 1629518528883,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008978",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "c7013179-201c-4a07-9b52-bba0f5730dc2",
      "created": 1629504144644,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009229",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "83b16497-78e2-437d-a8d2-ff35738d6e15",
      "created": 1629489773256,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009963",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "8e3ee58f-a440-485e-bebf-d31e6dd18704",
      "created": 1629475389127,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009599",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "82f744ec-bfed-4859-b91f-cd1f5bcd82a2",
      "created": 1629461016489,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008831",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "9c2321db-4ca5-44b4-ab6e-e5acbb9c1e9d",
      "created": 1629446590047,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009083",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "4ae6e5c6-15cf-444b-8136-a613c12ef4ab",
      "created": 1629432223949,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008960",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "7cbdc5fa-137b-4dbb-b2e6-3abd206d5fbd",
      "created": 1629417733757,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008997",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "7099c70c-cd6d-4a0a-ab38-749af1e23cd2",
      "created": 1629403363061,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009927",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "03ac6c00-3626-4bc4-8ade-2fba8548a8cf",
      "created": 1629389030885,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008816",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "b1f8ed13-7f1d-4b9a-b42f-22c46f52d571",
      "created": 1629374669011,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008818",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "baf64f81-45c3-4675-b1e0-3fd96d80a7ee",
      "created": 1629360230825,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009103",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "5658b3d3-cb34-48c8-be7a-0cb7a53ac75c",
      "created": 1629345804514,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009105",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "dbbf986d-8c79-49fe-a2f6-dff276937fae",
      "created": 1629331365080,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008987",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "c0d24a5d-099b-491a-8d1f-eefcd91b7784",
      "created": 1629316973133,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009710",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "738dc8a9-0359-4d73-88cd-1b2adeb7198a",
      "created": 1629302550128,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009127",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "579ab9e0-c1f3-4aaa-938c-d09643ec20a3",
      "created": 1629288169065,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006822",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "fb0fcbe9-0ea2-41b9-9544-acdebee25b15",
      "created": 1629273729445,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006683",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "2163bb9d-802e-45fe-9341-fa98a9384ea7",
      "created": 1629259322726,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007055",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "0248c203-84a4-4b53-954e-afa6dbbc696e",
      "created": 1629244916880,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009627",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "618d603c-0209-44dd-80ed-890bb25c854a",
      "created": 1629230537954,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "77a777ef-2b4e-4d41-a17d-c65658366d5f",
      "created": 1629216147860,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008813",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "bcb5125f-2e50-498e-b00c-e7afff82d2a9",
      "created": 1629201722878,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007293",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "04821c92-9c03-4d74-9a90-ef5a2781adcc",
      "created": 1629187289707,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007565",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "7547edb4-3d32-47c9-ad7a-e13c78385891",
      "created": 1629172873653,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009303",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "9970b8a0-403d-4061-aba1-c681c47e5c3f",
      "created": 1629158459949,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008695",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "b45ea71e-cfb4-4cd1-a2c6-382042984e06",
      "created": 1629144095486,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008757",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "6cc8614c-7dba-4964-8cf0-ae57e762b0a6",
      "created": 1629129693178,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009612",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "43141441-9e3d-483c-a12c-76c9eebe87ef",
      "created": 1629115319723,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009911",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "e06d7073-b155-4489-82c4-e17278bba780",
      "created": 1629100883517,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009846",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "7687da76-1da2-42a0-a3a6-866684bd55ee",
      "created": 1629086438272,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008005",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "5198a7f3-37ba-44a3-9490-87b5267de4a7",
      "created": 1629072022373,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008133",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "305849c3-ff93-444d-9079-8f1151f6431b",
      "created": 1629057641028,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010220",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "08114712-942e-4ab5-84fc-97e4b935558d",
      "created": 1629043286486,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009500",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "ea3cea64-b583-43fd-bf4f-776cacf68147",
      "created": 1629028866275,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009171",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "b995c383-baac-4726-a30f-a6620be924a8",
      "created": 1629014420275,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009128",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "2eab029e-87e2-4bef-8833-51479706f93e",
      "created": 1629000046821,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007925",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "32d42a71-5f23-41dc-9dc7-57e4a6973f40",
      "created": 1628985641535,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007460",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "2d02bcbe-c4a1-41ed-81d5-d18e9bb1f9d0",
      "created": 1628971287453,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008239",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "5a260385-6218-4016-9e0c-3fd34fe3c1d7",
      "created": 1628956843798,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009651",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "256aa6f9-2830-4be7-95fc-05bd69b12794",
      "created": 1628942686681,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007209",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "653e603d-81ef-4c2f-a20c-c5aa9e7d308e",
      "created": 1628928047989,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009490",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "741da58d-de4f-4d7a-b56e-87044675db84",
      "created": 1628913640577,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009313",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "8654a3f4-61c0-4c35-8d8f-1d8d3ee59746",
      "created": 1628899285387,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010408",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000208
    },
    {
      "id": "167d87e6-693d-425f-bd21-3d898e86b61f",
      "created": 1628884875068,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009931",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "2a07af0f-3caf-476e-9934-b4a39ad45e66",
      "created": 1628870418291,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009661",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "69a736eb-602d-4798-90ba-e612a6c4d4d6",
      "created": 1628856040139,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009605",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "308a5786-ce69-4bdc-9a02-9c24ce951d38",
      "created": 1628841652158,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009383",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "7f532385-12ca-4601-bfc6-9a5c272fdc9d",
      "created": 1628827411289,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009261",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "6798179b-29bf-4ff6-a0db-5a5e048dcb8d",
      "created": 1628812969386,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011016",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "c42a3da6-5033-448a-9017-9805a4c42e4b",
      "created": 1628798593418,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009550",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "9441d6b0-abc5-431d-984f-6dac9d777270",
      "created": 1628784182846,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009459",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "293b73d0-5338-4981-a03b-0a1735854407",
      "created": 1628769838487,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009780",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "b843a876-e85b-42e5-90b8-564737e4b5c7",
      "created": 1628755462281,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009729",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "782a6e17-0b13-423f-ac1b-4b57c1d4fced",
      "created": 1628740988489,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009268",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "1068c118-8b61-443b-afab-e7d0392e8812",
      "created": 1628726594268,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009928",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "cffc2ff6-abc9-4b9e-b87f-fdedea9cd478",
      "created": 1628712214518,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010989",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "fd5ceb9f-b3ca-4528-bd5f-3a31d23577e3",
      "created": 1628697775322,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010029",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "90e2d5e7-cca8-451b-91f8-1684c886ed47",
      "created": 1628683390536,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009808",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "6a9a032d-17da-4267-a451-558c5dde1c65",
      "created": 1628669010884,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009668",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "34a87d1b-a41b-4ac4-b305-aac9a7b6c733",
      "created": 1628654596498,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008725",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "5901c0ab-cf41-418e-a7a3-d9817a143263",
      "created": 1628640267352,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011289",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000226
    },
    {
      "id": "f997c66c-72c8-482a-ae82-2c90bb6321a2",
      "created": 1628625828403,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009313",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "48c3e142-1b11-4750-bd46-67a07e72357f",
      "created": 1628611423095,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009473",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "7d805f5c-743d-43d1-bd8c-7a8b7fa1b94a",
      "created": 1628597122008,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006804",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "4f2379cf-170d-4bc0-a97e-4c0f4ac26a5e",
      "created": 1628582771258,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006730",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "a4da9ddf-5f44-4e3b-898f-947b71311e7b",
      "created": 1628568220947,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006774",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "13ac9bfc-177a-4f6d-8d8b-1b576939f516",
      "created": 1628553835489,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009163",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "e19cdb94-999c-4790-abf7-65b9b2367469",
      "created": 1628539443614,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008394",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "eb71196d-3229-4a10-8ead-7007757092b6",
      "created": 1628525066687,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008122",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "c8649cdd-cd82-47d2-ae69-8ce98c23bcff",
      "created": 1628510695793,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008091",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "0e4c87de-8bba-4cea-8564-f88a720f670e",
      "created": 1628496176845,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008583",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "7cde2716-86ec-4901-a12b-82325d583051",
      "created": 1628481776335,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008649",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "cc8b98f2-4896-4a9f-b699-670dbb8ec88f",
      "created": 1628467369680,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008607",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "79e018dc-b7f6-4cd4-8c39-1c6f5c9169d1",
      "created": 1628453018106,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009408",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "469a6c0c-c20c-4004-a2fa-f28dd6ae97f0",
      "created": 1628438560275,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008671",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "81ba9365-4602-48cc-94e4-02903a2b3895",
      "created": 1628424189274,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008216",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "0962e038-4592-4315-8618-72186b7289bc",
      "created": 1628409834272,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008213",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "c38f72a3-6c8c-44d5-9afd-be44312eb3b9",
      "created": 1628395432740,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008431",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "6a1a052e-83ca-4596-b7d4-92022d2e462e",
      "created": 1628380985499,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008508",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "53f4d806-e3a6-4ab6-bd48-273e616b957c",
      "created": 1628366707056,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008348",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "c81f4e0b-216f-470a-b008-f050ec767309",
      "created": 1628352163446,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008200",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "70702c0f-1248-4bc8-a325-bea1886ef9dc",
      "created": 1628337801780,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008008",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "5a447c50-257d-4c83-9a16-7f1da28b755d",
      "created": 1628323375345,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "180cdecb-c24e-4033-a122-0c177dc96a0a",
      "created": 1628308958600,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009030",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "24eedaa0-585f-4afe-b5bf-f430a0f8b582",
      "created": 1628294604308,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008744",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "0ea4e826-9041-4af7-b243-453f250751f3",
      "created": 1628280229185,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008833",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "15f07643-1995-4a47-a30b-c7da481e9e2f",
      "created": 1628265740574,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008674",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "5fbd92d1-9fdf-477a-8a92-a066b7a49357",
      "created": 1628251386443,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006422",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000128
    },
    {
      "id": "e85cb6c3-a826-4695-a46b-57bda0c4c1b1",
      "created": 1628237163589,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007566",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "1527b10b-5d1c-4b6c-b3f0-28636cb729ca",
      "created": 1628222708498,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008780",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "bfa0e3c8-f847-4c6e-89c2-2f657036339a",
      "created": 1628208198647,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009377",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "5ce111e4-4d4a-4d8e-8878-4cb167f834f0",
      "created": 1628193749535,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010037",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "e70d201c-6f38-46ae-a3e7-11d413d0a815",
      "created": 1628179380030,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009528",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "a10ee9c3-d69e-48b9-99e0-d1a2d289c905",
      "created": 1628164953305,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008032",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000161
    },
    {
      "id": "fe456a54-35c4-4429-8890-f65c0299b012",
      "created": 1628150560932,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008536",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "24169c96-adb7-4547-b18b-3ffb2d79c3e4",
      "created": 1628136171811,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010488",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "7873dd4c-b30b-4c74-a01b-48c0dc7a10ab",
      "created": 1628121789549,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010649",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000213
    },
    {
      "id": "7bfb52d1-2a4b-4feb-955f-4a056940d5bc",
      "created": 1628107343305,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011294",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000226
    },
    {
      "id": "2679a98d-63d5-4873-900d-a04388bed68c",
      "created": 1628092887481,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010234",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "a1a1a0ec-9586-45e3-b3a4-0a992a194b4e",
      "created": 1628078677804,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007700",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "fd42cf2b-8a4f-4de9-b331-fe4d572414cc",
      "created": 1628064114282,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009747",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "ed2b4bb9-f385-49e5-9b5f-791e0b8547b4",
      "created": 1628049750947,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009440",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "df58b4e8-6025-4bf8-a22e-7823cacbcd5a",
      "created": 1628035382758,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010356",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000207
    },
    {
      "id": "927b5972-25aa-480b-be23-48f507ed9580",
      "created": 1628020999401,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012379",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000248
    },
    {
      "id": "79eca5cb-5a30-4113-a352-1b69927e8db8",
      "created": 1628006567200,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010887",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000218
    },
    {
      "id": "3f903d6f-38b7-476d-889c-aff0436e60ef",
      "created": 1627992144154,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009969",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "47df1124-65e4-463f-882a-e1f2b88436da",
      "created": 1627977793361,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010255",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "714b2159-45db-40ce-8bda-a939ec09e8a5",
      "created": 1627963365257,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010223",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "19301fc1-6159-49a6-b397-453328aeb95b",
      "created": 1627948914857,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010529",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000211
    },
    {
      "id": "4da71fac-4937-4a1a-b04b-2c1274f4a764",
      "created": 1627934495078,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012696",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000254
    },
    {
      "id": "bf2d6090-581f-4e9b-b4fe-90baea20bb41",
      "created": 1627920084134,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010134",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000203
    },
    {
      "id": "8f39a29b-cc22-4351-955c-d1043381c281",
      "created": 1627905822628,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009659",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "2a397a57-09a2-4b6b-91fb-c02a8f888949",
      "created": 1627891373735,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009815",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "e2244f1b-9189-462f-9ce6-4baccc6c77a3",
      "created": 1627877009056,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009836",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "595044ce-8888-4ac9-9c79-4eb037c7b1a5",
      "created": 1627862577737,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010491",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "b4616756-970c-4a48-9412-cf0ca6c63410",
      "created": 1627848104142,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010437",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000209
    },
    {
      "id": "44b629f8-2086-4dbe-882a-16f6da2d2caa",
      "created": 1627833786542,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009778",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "e666e236-701e-490e-9ced-daee94cb2fd7",
      "created": 1627819343986,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009118",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "72e8de48-2fb5-4c81-9852-b4de2be92360",
      "created": 1627804955700,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009220",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "6a4ba882-0070-4135-a3ff-cab4717462ca",
      "created": 1627790699523,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009179",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "19e01166-85f2-4e4f-a501-b91fd90f5199",
      "created": 1627776155412,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009731",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "9749711d-65c0-4393-bdff-9ecb2916bf87",
      "created": 1627761782317,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014170",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000283
    },
    {
      "id": "2429ec96-e4cc-4394-8735-b907f488d69f",
      "created": 1627747387274,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008633",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "007159be-488a-4777-8af1-3c5d2009ca75",
      "created": 1627732959478,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008864",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000177
    },
    {
      "id": "f1a0359d-17f2-4558-abfe-46fab851f1aa",
      "created": 1627718501645,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009055",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "662e5ba7-75be-4d15-a331-933eb86089ad",
      "created": 1627704148683,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009969",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "176f5ead-8bbe-4277-a389-607016232b20",
      "created": 1627689722612,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010748",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000215
    },
    {
      "id": "9e2c91db-4b5a-4bd0-baa3-39f69039dd7b",
      "created": 1627675294464,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010804",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "2e30dafc-5ad6-4c88-988d-bf296348d444",
      "created": 1627660891644,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010669",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000213
    },
    {
      "id": "33dcbdac-0497-44ec-b0c8-91923495bf51",
      "created": 1627646528828,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010517",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "57981716-429c-476f-8d65-1975a25c9668",
      "created": 1627632128816,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010686",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000214
    },
    {
      "id": "49f96be1-41c1-4ec4-b080-3e143fb478fd",
      "created": 1627617738291,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010844",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000217
    },
    {
      "id": "617bb241-688b-4275-83e1-43eef1dedf0d",
      "created": 1627603291300,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009808",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "ae32142c-63fb-4bd3-a809-be40c063cbfe",
      "created": 1627588912598,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010059",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "de7996b4-5e36-4020-be99-9fc69877fc41",
      "created": 1627574631113,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009348",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "608d78ec-987a-49ff-b912-c14c6014815b",
      "created": 1627560222436,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008756",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "1e8c3a4e-d49c-454d-bfa6-2335b97e2cb1",
      "created": 1627545830985,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008433",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "73e01316-cb52-4544-b26d-2a1123fcb2e1",
      "created": 1627531397733,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008506",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "3760ab02-fc9f-4868-bdd2-056bbd8d97bb",
      "created": 1627517021523,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010687",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000214
    },
    {
      "id": "eb703e3b-c10e-4fdd-8976-33b7e2adfb4a",
      "created": 1627502644782,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011753",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000235
    },
    {
      "id": "d76bc967-5895-42ab-bbd8-9d3a17e44d60",
      "created": 1627488119935,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009978",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "7b627daf-020d-405d-8b8b-e892d8405296",
      "created": 1627473797497,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008334",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "4e34a2d1-8b81-4f16-96a4-f7ec9f99c224",
      "created": 1627459331993,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006941",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "22d9b1ae-12f2-4717-b18b-9a7e2be06238",
      "created": 1627445033197,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009787",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "87806605-be93-4286-bc0e-384ea343aa74",
      "created": 1627430595084,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012880",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000258
    },
    {
      "id": "16472a65-801c-4008-8bec-af8762181d86",
      "created": 1627416431582,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009091",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "33ebe019-bba2-4bbb-b9c7-05a3685c9926",
      "created": 1627401886791,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010233",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "640b260f-0aae-414b-92c2-5aa59b756cd3",
      "created": 1627387428669,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007549",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000151
    },
    {
      "id": "eb4be2c5-2303-4db1-bcb5-14f4bb1f8eeb",
      "created": 1627373024853,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006279",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000126
    },
    {
      "id": "2af11c41-4c8f-43d7-b0e0-4e8254386f5c",
      "created": 1627358582305,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008378",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "0eca396b-4c8c-4690-b5ec-18f5d68204c6",
      "created": 1627344204215,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009928",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "efd1bac7-a9b2-43d1-8286-dcc07b3d1131",
      "created": 1627329792863,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008335",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "c4842f42-3a4f-4e0b-a2a6-ce991ec525d3",
      "created": 1627315370308,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009827",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "fd5cc4e2-fdc1-4708-9ee8-aa9f6f64ffe3",
      "created": 1627300979874,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009195",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "8f18505f-88ea-48e0-81b9-8b7462e2dfa3",
      "created": 1627286625922,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009306",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "d9848791-f255-4e07-8db4-41ef9f65bb35",
      "created": 1627272097006,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009761",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "d5172faf-aca3-454a-b2e5-e6cff92cfd1c",
      "created": 1627257712375,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008975",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "ad508788-e018-4fa3-bf6d-6f7651ace389",
      "created": 1627243353644,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009744",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "877ea698-a486-4ec5-ae86-5567778ee854",
      "created": 1627229025625,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009267",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "58268cfe-39fc-4a2d-94f9-1e525b13d9ff",
      "created": 1627214588817,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009121",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "abd004b4-dc11-45e5-bfd8-50b5c3c1f6dc",
      "created": 1627200147308,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008641",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "905a5d5f-4706-43d9-bed0-c1db9b923b88",
      "created": 1627185753054,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008949",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "1e5afd34-722b-4a96-af57-85bd4b515c67",
      "created": 1627171370663,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009059",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "c43d4f6d-6c45-401a-8ef5-c2034fb4500d",
      "created": 1627157001590,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010919",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000218
    },
    {
      "id": "94997c37-a5d9-4221-8c79-3869f56d7e66",
      "created": 1627142664845,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009681",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "01282f28-f35b-41f0-9364-8497db8bbac3",
      "created": 1627128153374,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009254",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "11290ee1-20e8-468b-9c52-397f0ed33bb0",
      "created": 1627113777054,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009303",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "4428c8e3-40b5-4f12-b7ce-f40ca2351729",
      "created": 1627099384095,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009920",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "f1baa788-7ce8-4e96-a9d8-e789c134dac9",
      "created": 1627084920380,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012448",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000249
    },
    {
      "id": "2a96b971-3f4c-477f-8683-fb4ade915a3e",
      "created": 1627070501267,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012060",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000241
    },
    {
      "id": "f72d010e-1f0b-4458-8ff9-76ff7672441b",
      "created": 1627056112993,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009604",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "39cb7746-697a-4e9e-b849-537c9b2680c0",
      "created": 1627041728956,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009293",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "bc9ccfe5-1c78-4321-aade-49715d730fdc",
      "created": 1627027410740,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009690",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "7258bc0d-7d8d-4b7a-b0dd-830be4caee46",
      "created": 1627012894569,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009461",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "b0e01ef1-5d9d-45d5-b6f1-8518e928ee8c",
      "created": 1626998521713,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011440",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "3f67f6f3-57f0-4668-84de-1464c47f7921",
      "created": 1626984119787,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009976",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "d46e9535-9315-452a-a1a5-474c3f203a60",
      "created": 1626969704447,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009302",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "b5d2b719-d863-464e-a777-0e253487d470",
      "created": 1626955332771,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009889",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "b6714f80-7b7c-42eb-9c68-2d2ca7cd996b",
      "created": 1626940848243,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009668",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "fb555822-bd43-48e0-b7e2-4bfaceabe6a0",
      "created": 1626926421940,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010119",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "f4ffec7f-0a7f-49fb-8cdc-76714efd01a0",
      "created": 1626912032537,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010046",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "ff7e74b5-9659-4a2f-b7ee-88bcadaa0aea",
      "created": 1626897630112,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009802",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "19a5dc14-f864-419a-98c4-e0c5c0e72c5e",
      "created": 1626883252734,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009019",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "206ba3e9-5a39-48d1-9d86-1bfc3575be48",
      "created": 1626868871373,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009202",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "7d81ac72-1880-4957-b5c8-657b08941656",
      "created": 1626854567919,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009536",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "7e47a39d-133a-42f3-a30f-7183ba8ff46a",
      "created": 1626840017426,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009439",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "c203d6db-9fbc-4929-8943-d32be7e67427",
      "created": 1626825641623,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008920",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "3b8d2697-b106-42f1-8060-630a6a959030",
      "created": 1626811273615,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009180",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "3f21d2b6-2b3a-4640-8e74-da734ce4f12f",
      "created": 1626796839486,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008466",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "e28ace2e-3d95-4363-8ca0-bab11f28fa17",
      "created": 1626782497010,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008780",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "2474ea69-e3da-442e-ae94-ad5f7d056a7a",
      "created": 1626768036613,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010716",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000214
    },
    {
      "id": "02b10d38-9bf5-4951-9011-bf907ad1dfc1",
      "created": 1626753643804,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009820",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "f29c5d79-c948-4432-8a21-46f67e2bfd2b",
      "created": 1626739208899,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009511",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "fa618faa-68bf-40c8-88b5-8c5f7ebb37e9",
      "created": 1626724897014,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010008",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "1f46cc92-81ec-48dc-a2fc-b2b8b2f9d34f",
      "created": 1626710537540,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008532",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "96161e24-2766-49c5-a85c-048f4f99a12c",
      "created": 1626696052396,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007111",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000142
    },
    {
      "id": "ccaf6a99-6602-4b1c-a0b9-5c802cf6beff",
      "created": 1626681646949,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009083",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "7988d212-ff5d-4a15-89db-42d2c794fbf8",
      "created": 1626667534011,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009214",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "216bb58a-51f4-4800-b739-a9a5934898cf",
      "created": 1626653114345,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009644",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "ce04051b-d1c6-4e79-a5dd-34d014116b0e",
      "created": 1626638474728,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009808",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "d12fa4ae-6ab5-4507-ae09-ca8f22d4ed25",
      "created": 1626624284764,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009329",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "3a142f91-9f78-4e5b-b003-ee20d92fbccd",
      "created": 1626609843165,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009611",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "a4afe99e-8b27-45f5-a62d-bf86c0a27ffa",
      "created": 1626595564659,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009710",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "f608fe62-7921-4b48-aaaa-d51aaaae0c3c",
      "created": 1626580998673,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009599",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "628df4de-e9bd-4321-82ce-d965ea05787f",
      "created": 1626566650616,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008165",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "d1ca4570-7b24-4534-b8e3-cf17c097c9d2",
      "created": 1626552178293,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009147",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "552c2db9-526d-4951-b332-3ae294eef81d",
      "created": 1626537862704,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009510",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "e0622353-b768-4d30-bed7-6e7f315b2905",
      "created": 1626523484586,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006822",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000136
    },
    {
      "id": "d6723c7c-8099-454c-8718-28d68bd4efe0",
      "created": 1626509132640,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006722",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "9e3100af-33ef-49a6-b6d9-f4126546d670",
      "created": 1626494739595,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007816",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "46b5af28-6ab1-43f5-b3ac-aba71fa3fff2",
      "created": 1626480305274,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010405",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000208
    },
    {
      "id": "7f2a3cca-d8a7-4568-a6cd-e0f4bc291594",
      "created": 1626465888573,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010772",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000215
    },
    {
      "id": "9f0c715e-168f-4651-a714-1a6da988ed3c",
      "created": 1626451478424,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010593",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000212
    },
    {
      "id": "3fd49b22-efd8-4240-944d-fdd4248ed04b",
      "created": 1626437051148,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009966",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "71228afa-8431-41de-81a8-1cfd358fb48b",
      "created": 1626422658329,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010986",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "48ce3972-cc13-4b77-83eb-6fd3071fbd4c",
      "created": 1626408239774,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "9f99e672-1605-434d-8549-cff83bf0d379",
      "created": 1626393791173,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011626",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000233
    },
    {
      "id": "7da4f0f7-774a-4084-aa9a-9fa833a716f0",
      "created": 1626379457516,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012835",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000257
    },
    {
      "id": "b976fde9-f92b-4585-a759-246f4bbbe4e9",
      "created": 1626364854951,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012544",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000251
    },
    {
      "id": "9110f61e-470b-4a4d-90e4-ad67a28a1762",
      "created": 1626350796711,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006406",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000128
    },
    {
      "id": "cb9e07b3-dede-4a58-8772-954ce53dc3ec",
      "created": 1626336246497,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011097",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000222
    },
    {
      "id": "ea6937fd-fd06-4404-ba2b-ade6faaa7206",
      "created": 1626321808742,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011382",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000228
    },
    {
      "id": "2a001cf6-d79a-4ec5-a84d-1a21471af85d",
      "created": 1626307401680,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013199",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000264
    },
    {
      "id": "4e26c03a-46a6-4449-98ed-fb800b0180ee",
      "created": 1626293155166,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012468",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000249
    },
    {
      "id": "15f4a3b5-cf2b-4804-8c8e-3ad5ae3237ee",
      "created": 1626278619558,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000239
    },
    {
      "id": "701a46de-786a-4274-a24c-e90f8cc969c4",
      "created": 1626264246278,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011339",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000227
    },
    {
      "id": "40427555-78ae-41bb-9cfd-8df2028af2cc",
      "created": 1626249896199,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010862",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000217
    },
    {
      "id": "602750bd-c740-488b-938b-5c6e564f83cf",
      "created": 1626235434743,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010811",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "f2cdec01-1dcf-4a7a-a0f6-e5b151143857",
      "created": 1626220997810,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010800",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "282f2ce6-cad0-45d7-a94d-515a1dd790b0",
      "created": 1626206578916,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010873",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000217
    },
    {
      "id": "6ef4a830-e032-4c08-befd-79175ab33f5c",
      "created": 1626192227206,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009070",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "bc2c4786-e684-4f25-a820-9cca93716100",
      "created": 1626177819325,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007959",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "6b639b93-9d86-457e-961f-b133a789aa92",
      "created": 1626163392263,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009911",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "15ff9453-84a8-484f-a041-fafde0fd5f3b",
      "created": 1626148998481,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009920",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "82db6c85-e250-477b-886c-ba99cabb48da",
      "created": 1626134515552,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009975",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "95a196fb-8807-4dd1-a36f-7fa55c0f8a61",
      "created": 1626120191672,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011808",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000236
    },
    {
      "id": "7bc98940-5a34-4452-ae79-863355bde2f9",
      "created": 1626105829001,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010662",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000213
    },
    {
      "id": "421100ea-8619-4539-b335-2417f1ebed59",
      "created": 1626091362605,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010063",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "cb8d3b0f-cb80-4c95-bbfc-8acb0fb02e62",
      "created": 1626076975710,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010063",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "d3257495-98aa-45f9-8204-a52610e25991",
      "created": 1626062585972,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009891",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "ea58c66f-5210-4cfe-aa6f-e21e489969c2",
      "created": 1626048134169,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009568",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "e2f50038-dce0-4058-96a0-a272b6288c05",
      "created": 1626033756883,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009505",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "d13198aa-b67f-46ab-8cc3-cfbd0edd0bf6",
      "created": 1626019386651,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006270",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000125
    },
    {
      "id": "17733df2-25aa-4369-9ded-0f1a337d1f45",
      "created": 1626004931701,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005405",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "4f71f696-1d56-4eea-bcbb-01b76d533d8b",
      "created": 1625990676102,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005154",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000103
    },
    {
      "id": "aa89c4df-2c78-4e90-8f77-11a06ea3ef83",
      "created": 1625976258778,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009321",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "86f7991a-01e3-40de-8406-e7fa5b6c5c32",
      "created": 1625961795738,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009798",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "92e47258-9c7f-4193-8deb-7d49c9afa80c",
      "created": 1625947430339,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010077",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "359e7d2a-e14b-4f3c-8624-e4be1e647f45",
      "created": 1625932974118,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010030",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "7580fc57-cef0-4fce-9b69-25bc5cfcdcc2",
      "created": 1625918600709,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010022",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "c598264b-47a1-4c52-b209-dd07a432e813",
      "created": 1625904183571,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010261",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "0441159e-96d7-4e1b-a9ff-79b0fd9bfcc9",
      "created": 1625889783733,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010635",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000213
    },
    {
      "id": "c84f7415-548f-49f4-a97c-406c4a6f6c4e",
      "created": 1625875403758,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010970",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000219
    },
    {
      "id": "98cada2a-f247-4964-b45c-0413535eda3f",
      "created": 1625860995574,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011408",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000228
    },
    {
      "id": "31d807ff-ebab-4d66-ad97-caf2bff6f2dc",
      "created": 1625846638079,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011625",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000233
    },
    {
      "id": "f2ab4ad6-8d07-408b-a182-f6ee4bc4d448",
      "created": 1625832187343,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010964",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000219
    },
    {
      "id": "0d125c6b-bc44-43cb-96c6-24857217e8ad",
      "created": 1625817851192,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011487",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000023
    },
    {
      "id": "00243032-1268-4f9f-9f01-5f0301ece6df",
      "created": 1625803355316,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011393",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000228
    },
    {
      "id": "3599c245-2a2c-49c0-8970-ea4dad8940b8",
      "created": 1625788988560,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012596",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000252
    },
    {
      "id": "5ee1c9e6-0842-4088-a074-ad8870d57526",
      "created": 1625774643328,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012495",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000025
    },
    {
      "id": "394c0cb1-ce8b-456e-a162-247d6272bb0e",
      "created": 1625760233062,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012578",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000252
    },
    {
      "id": "bf4665e3-8b1d-4345-abc4-7c493b0e2d23",
      "created": 1625745863407,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012540",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000251
    },
    {
      "id": "6ec0de97-2976-4347-9bcf-317eaf2a6003",
      "created": 1625731471230,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011095",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000222
    },
    {
      "id": "7a23710f-fd8b-4e3e-a6f1-aa5e0feb0c7e",
      "created": 1625717031872,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011667",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000233
    },
    {
      "id": "dc4aa193-98cc-47ef-8cf4-012b272eb67d",
      "created": 1625702587852,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011907",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000238
    },
    {
      "id": "7f037eb4-b990-4da2-a942-fdab42e40ee4",
      "created": 1625688152994,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012814",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000256
    },
    {
      "id": "e6d2eb57-1393-4787-b1f5-54fbda6466d4",
      "created": 1625673865505,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013225",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000265
    },
    {
      "id": "15e5ede1-1651-4943-ab06-ab5703947b13",
      "created": 1625659400337,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011425",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "f79853c5-7d08-4d91-bedf-15e8b67ebdba",
      "created": 1625645086490,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013026",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000261
    },
    {
      "id": "918bf5d0-4064-4acf-a17b-928e052e51af",
      "created": 1625630602325,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012622",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000252
    },
    {
      "id": "249b707a-5d8e-4a57-be25-c8c35c0d07a2",
      "created": 1625616272249,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013529",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000271
    },
    {
      "id": "67a674c5-62cd-4b25-9fa7-ae1cd2ff70b3",
      "created": 1625601930669,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014889",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000298
    },
    {
      "id": "b7d4c88c-784b-4d5a-bcfc-39c4f5b9f4cf",
      "created": 1625587432894,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010943",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000219
    },
    {
      "id": "dee6a044-339f-418d-a88b-e467c5cdb66e",
      "created": 1625573101808,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010916",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000218
    },
    {
      "id": "1fc3bf98-9e34-42cb-96ad-9a3652b16d9e",
      "created": 1625558822358,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008388",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "ba9d3d9d-0870-4e66-8c35-454441b4a1b8",
      "created": 1625544200812,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009322",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "47f7c7d1-45c0-4a96-b9fa-7798466a6096",
      "created": 1625529782032,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011731",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000235
    },
    {
      "id": "33a56bdf-a39b-4683-9332-9d8f8f0465c7",
      "created": 1625515400233,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011214",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000224
    },
    {
      "id": "7e946b79-4658-4223-8633-8f92caef91c9",
      "created": 1625500917436,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010011",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "17ba7a39-59d8-4ad1-9b7e-ed648b170c86",
      "created": 1625486615213,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007815",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "7977d392-0251-408a-9ee6-aa02b900c01b",
      "created": 1625472260395,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007804",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000156
    },
    {
      "id": "04266b6c-6f17-4f4e-95dc-2fc088d50a4d",
      "created": 1625457797579,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007648",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "eb81f97a-dd17-48e3-8f0d-a96afccc1671",
      "created": 1625443410788,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007601",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000152
    },
    {
      "id": "18cb3ad9-cfeb-4182-a9cd-bef400070603",
      "created": 1625429107509,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007738",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "7dd29516-3d5b-4a06-b194-75b3d02cfd40",
      "created": 1625414568861,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007922",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "42f6434e-a9c8-41f2-a045-9caf614d1835",
      "created": 1625400135022,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007712",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "a1315f4b-baf7-4115-b28b-a40567eb5772",
      "created": 1625385952689,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007448",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "31b16202-4223-4951-952f-31f61bcb4778",
      "created": 1625371322765,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009206",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "eefddf3f-49d5-4f88-ada1-89e3326f64ca",
      "created": 1625356924793,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009798",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "972e22af-4913-41d9-87fe-1e2e0eef4852",
      "created": 1625342525499,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010213",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "31f627ec-db56-4671-afd0-bfd82bb5f480",
      "created": 1625328153504,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009832",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "ed6ccac6-2a0a-4d94-9270-d28f0fa22031",
      "created": 1625313850211,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009829",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "d2aab851-e976-4a15-89a4-9e6af64ec667",
      "created": 1625299485966,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009237",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "9f632d4b-6c02-411f-9a1a-d125bcbcf68d",
      "created": 1625285074104,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009213",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "3fb9523e-48c5-468e-adb6-dd973c259f9e",
      "created": 1625270590082,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009439",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "0edccb67-c90e-4c2c-9f87-8283583189d0",
      "created": 1625256143337,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009385",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "feb6716f-8786-4a6a-a363-986a0137f337",
      "created": 1625241828194,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010360",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000207
    },
    {
      "id": "50363381-0b6d-4d70-8981-d5687666a10e",
      "created": 1625227360087,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009539",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "fd025a4d-c394-499c-86eb-7abbd0534686",
      "created": 1625213022700,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009642",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "7d2c01d6-d2bf-4ea1-b7f2-2e7d95a90483",
      "created": 1625198557656,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009825",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "1bfd246e-3538-4a59-967e-44ccd18be92b",
      "created": 1625184198424,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010240",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "77183540-53df-4226-834d-3c9700d55751",
      "created": 1625169794578,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008395",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "e97c7e42-0a3f-4b68-af8b-ae5d2c65e245",
      "created": 1625155457001,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009836",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "1f9dd8f3-3d29-49f3-a8a1-faffa2168d91",
      "created": 1625141020899,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010131",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000203
    },
    {
      "id": "e493f34a-64be-4b92-bfe0-e343345fca75",
      "created": 1625126570021,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010076",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "764c42cc-4cbb-446f-8ced-f3f917a35cae",
      "created": 1625112186500,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009857",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "4e7b28a8-cdf8-4db8-ae8b-5412653b4b14",
      "created": 1625097765729,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011438",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "56ce8245-2e31-4d8a-b93d-ee351fbdd381",
      "created": 1625083399059,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013103",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000262
    },
    {
      "id": "6a4bcd9d-abd0-4bc3-8c43-21d3720ef8eb",
      "created": 1625069062289,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009748",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "69c4e2a5-4d33-4e35-a2b7-0ca0f5cb1417",
      "created": 1625054653551,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010908",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000218
    },
    {
      "id": "5291c20e-2813-418c-b872-8719a9ebcb46",
      "created": 1625040221733,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010355",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000207
    },
    {
      "id": "75cf7271-c2ca-4c63-92ee-48bca339f797",
      "created": 1625025780509,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010025",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "99987767-8e56-4cdd-8498-5ae54a34e7d9",
      "created": 1625011343595,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010812",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "bd41e3ff-ca9d-48a9-927e-35898bae3d45",
      "created": 1624996943359,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011090",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000222
    },
    {
      "id": "7799bb7a-7678-46d3-92b1-eff7fc3b93a6",
      "created": 1624982627552,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011329",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000227
    },
    {
      "id": "b391e0df-6481-4527-aa72-2ad68771384b",
      "created": 1624968300205,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010700",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000214
    },
    {
      "id": "28fdf1b4-caf1-4c85-971a-3d0fa638e999",
      "created": 1624953731460,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010235",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "121158ce-cbb8-4bb5-90ca-7c41f80a468d",
      "created": 1624939322305,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010452",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000209
    },
    {
      "id": "4bd774b7-d599-4c84-9e1b-337513bcd032",
      "created": 1624924904543,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010928",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000219
    },
    {
      "id": "96edb686-1849-404b-9353-9816ad558f87",
      "created": 1624910526928,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011402",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000228
    },
    {
      "id": "33906122-ab32-4716-9f81-a5bca367cd0e",
      "created": 1624896219710,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009194",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "66c4e516-14f6-429e-ae11-be37e2feed83",
      "created": 1624881742503,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010074",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "f81e2e83-8f85-442f-8b7b-8972fd4c47c7",
      "created": 1624867319921,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009498",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "d6ae4eed-bf8a-4ed5-b8dc-0163cd9da596",
      "created": 1624852903899,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009660",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "b425a116-c05e-44f7-a56a-2a661b57fedf",
      "created": 1624838519190,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "38ea19d1-49f6-4b6f-8669-6a04fd856998",
      "created": 1624824133800,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010536",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000211
    },
    {
      "id": "b14f5889-8fe9-4085-911e-18b361798ecd",
      "created": 1624809721398,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007138",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "fa76e74c-11f0-4cf6-bb55-ed556d43ab72",
      "created": 1624795331264,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007054",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000141
    },
    {
      "id": "545832e2-fc8a-4802-b526-75ba2fef6388",
      "created": 1624780944792,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007359",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000147
    },
    {
      "id": "bedfe31b-42ea-457f-9124-848f5db2ae1a",
      "created": 1624766534284,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007310",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "017d13f5-859d-45f2-b8fb-ed4250b874e3",
      "created": 1624752144737,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007241",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "5781cc79-97f5-4ebe-872a-9dd625ac9291",
      "created": 1624737766670,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007239",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000145
    },
    {
      "id": "a833355e-1348-42b5-8064-276feafa74ea",
      "created": 1624723410941,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007628",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "039a93ec-d2bf-4556-9666-8919c1eb10f6",
      "created": 1624708923492,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007476",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000015
    },
    {
      "id": "6a375525-a3fc-43be-adb8-803b859df89c",
      "created": 1624694536684,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007317",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "656b2622-0448-4fc7-a6ad-595dea14a093",
      "created": 1624680116008,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007697",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000154
    },
    {
      "id": "e257333c-696f-40ae-b45a-12389ce0799f",
      "created": 1624665709009,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007911",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000158
    },
    {
      "id": "7d453674-6274-421a-995e-56b4f9c87658",
      "created": 1624651326342,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008613",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000172
    },
    {
      "id": "99ef857b-5420-448e-8448-7b5f1187d476",
      "created": 1624636958306,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007988",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "7f2adb12-558a-47a8-b1d6-091849f04ac6",
      "created": 1624622629811,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008190",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "c2f0fe4a-b373-4869-87ef-6b7972e26b74",
      "created": 1624608114610,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009591",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "98f9f143-d8b3-4fa4-b18e-d1a2dcbce2d5",
      "created": 1624593713981,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009300",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "6ab4ecd8-32de-4858-89cf-651fa6fa0dea",
      "created": 1624579342149,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009967",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "27c617d5-d210-4949-bdf5-2f192cfbd8e2",
      "created": 1624564963517,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008264",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "d5c19dc1-90bd-44f4-aca8-273362450deb",
      "created": 1624550538884,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010204",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "53978b93-335a-492b-9c42-2d4844a14647",
      "created": 1624536182699,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010041",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "b728b8b7-61be-4537-8706-26b446a8d8cc",
      "created": 1624521720241,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009903",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "f4c4b13c-0a03-4ebf-ac1f-0bc0590f17a6",
      "created": 1624507362426,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009609",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "f014f1eb-2b7f-4fd2-b55d-7ef04a88a583",
      "created": 1624492974416,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009955",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "08923672-2107-4d96-9168-8421c75ccb3d",
      "created": 1624478549751,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010480",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "3bf24eef-d965-4116-9038-eb6952991676",
      "created": 1624464121027,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010365",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000207
    },
    {
      "id": "9ffb3589-bc26-45f7-b688-b583a93abd23",
      "created": 1624449772118,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010213",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "6e15deaa-6a9c-4182-a08e-b19196cb7ad1",
      "created": 1624435337673,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010226",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "b4e5eef1-c8d4-4b27-9020-e9945e516cb5",
      "created": 1624420937926,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010274",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "68c8aaf7-6625-4ae8-8b3e-69b4d3b84ad3",
      "created": 1624406533199,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010381",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000208
    },
    {
      "id": "4a8045a1-f5f4-4625-9109-3c9fb7f4b23a",
      "created": 1624392118470,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010512",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "92cd2612-50a0-4953-918d-a8bb0e3a642d",
      "created": 1624377817030,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00018276",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000366
    },
    {
      "id": "db0dd2c5-1351-478f-b177-08d82b807ebf",
      "created": 1624363369997,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011186",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000224
    },
    {
      "id": "2465913f-fa33-4461-8ef8-8e7bca9cc5fe",
      "created": 1624348961029,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010498",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "3c4dd5c1-f570-4321-8266-43ee3744c894",
      "created": 1624334546636,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011986",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000024
    },
    {
      "id": "63310585-302b-41af-a575-1ae69b87e5d1",
      "created": 1624320290438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011291",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000226
    },
    {
      "id": "596a7426-bcf1-4997-9b59-aaa8af264eae",
      "created": 1624305735584,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011064",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000221
    },
    {
      "id": "cb29ffe2-5a8d-4d4b-ac79-9b99eccf60ae",
      "created": 1624291355386,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011171",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000223
    },
    {
      "id": "0cb3c6a0-823d-4a91-9a27-cb292a2ab89c",
      "created": 1624277057495,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009013",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "185ffeb3-fd6e-406a-90bd-a5b8738414e7",
      "created": 1624262571770,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007981",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000016
    },
    {
      "id": "d17cd9fb-c042-40f4-8e41-6ea9372de74e",
      "created": 1624248129764,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006774",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "2ea52ea9-c663-4ffa-ab33-ccf80f6faac6",
      "created": 1624233742932,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007947",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000159
    },
    {
      "id": "9d53338c-7942-4e36-b7a8-763b838dccea",
      "created": 1624219419372,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007151",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "d921dfd5-40a8-4ef5-9e13-d719a1bcea40",
      "created": 1624205063371,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007315",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000146
    },
    {
      "id": "bae771ac-36cc-4573-8144-615883a1e4c6",
      "created": 1624190534438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006758",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "7c441568-fdfa-43a9-bbe6-d13dbd8554b2",
      "created": 1624176195966,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006936",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "a00979c4-aaca-485d-8c96-5dfc9800dfd3",
      "created": 1624161736432,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006628",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000133
    },
    {
      "id": "0720101f-b88c-470c-a63c-5eed4bc908ee",
      "created": 1624147450871,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006922",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000138
    },
    {
      "id": "4c7f8163-a5c3-4124-b6ed-25373122bac7",
      "created": 1624132992869,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009017",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "ce34f8c4-0f8b-49d4-bde4-5b6ce2f3d86a",
      "created": 1624118634760,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009417",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "46a13928-cb41-4ee5-a5b5-f3bf69516503",
      "created": 1624104242061,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009280",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "4b00f05f-a705-4f19-93c4-d9a843e27bbd",
      "created": 1624089781370,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009680",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "9fd16809-bb40-49d1-bfeb-22c65597f855",
      "created": 1624075400572,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009064",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "1c83fe59-926f-4529-8ffe-ac4c0fa4930e",
      "created": 1624060996356,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009739",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "e6ec47b5-d707-4d27-a954-e741728aeab4",
      "created": 1624046600018,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009708",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "4e088e69-5ac4-4032-a4d2-021438c5a584",
      "created": 1624032270048,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009570",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "9a7c87c4-777b-4f2b-9eb6-5b3ea45ac0f8",
      "created": 1624017784773,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008749",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "f92232e6-6333-40d1-ba27-d356fc6514e9",
      "created": 1624003384359,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008556",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "4f11c8c1-222b-4504-acee-4103acb276ce",
      "created": 1623989015142,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009230",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "12654b23-f1ef-4c4d-a63e-65240d1d635a",
      "created": 1623974543707,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009268",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "2c03d6a1-6fe7-4839-80ed-fd85b59e912d",
      "created": 1623960178367,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010034",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "7ee21917-fc3d-44d9-b42d-43e4fc1d14e5",
      "created": 1623945757184,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009482",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "84892f17-db95-49ad-ad66-c57a13334f8e",
      "created": 1623931337299,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009460",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "566e2efa-53f6-490d-bcff-1a6e699683c7",
      "created": 1623917022699,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009654",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "7d096499-0bee-47b2-b89b-70a91c12c7cf",
      "created": 1623902523966,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009488",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "136734d6-fbf7-4c18-8e3f-17f83f989471",
      "created": 1623888180172,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009494",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "b18cc545-ae07-4c0f-be00-8c22492bdcf8",
      "created": 1623873750064,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009719",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "8800dc13-1544-423f-b876-40997d1c79e0",
      "created": 1623859419795,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009537",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "ae538ccf-805e-4afc-82b1-5d8be5fd019e",
      "created": 1623845048197,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009507",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "7a5c0281-ac69-45d7-9455-baf3af218903",
      "created": 1623830630749,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008985",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "405ac31e-7767-430b-b6c9-b6b20d1ecb48",
      "created": 1623816182821,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009031",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "0eb815df-3200-473c-8f71-3d62fd9713b5",
      "created": 1623801769132,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009583",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "98d14645-0883-44d5-83e3-2f3b056c56ba",
      "created": 1623787392229,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010204",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "4319ae99-3e8b-4c32-a8ab-b5c9791d8e67",
      "created": 1623772916294,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009723",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "3655e141-bdc2-4cfe-bbfe-8d4e549497ed",
      "created": 1623758662186,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009553",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "9134901c-d3c5-4900-b276-98752c890613",
      "created": 1623744114412,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009566",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "17b9a73c-f3d2-46d3-b6a8-eb930c73b4bb",
      "created": 1623729775854,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009874",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "ee041cb4-5320-4aea-8a9d-09913ba147bb",
      "created": 1623715338274,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009784",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "1b11e3f8-f963-4620-b9ab-022c5c6f9c2a",
      "created": 1623700911148,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010518",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "109fe860-97c9-41e8-8d0e-42c032237ccc",
      "created": 1623686603670,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010001",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "dafaa27c-493a-48ff-8ce1-3546cf8e3826",
      "created": 1623672125084,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009810",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "b0186ffe-460e-47ac-884f-b0531923e01c",
      "created": 1623657751651,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009296",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "8bf377bc-c121-4827-a249-56d32616230e",
      "created": 1623643388580,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009514",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "2975525c-8e42-4da1-bf5f-a179b801d916",
      "created": 1623628930329,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010342",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000207
    },
    {
      "id": "6594885e-9187-4006-9a13-855b9890207c",
      "created": 1623614574835,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009610",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "fd05e1f5-1416-4f12-8858-5e3b6a8b14e0",
      "created": 1623600166091,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009693",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "a454b918-015f-4353-824f-c0a11aa62a78",
      "created": 1623585723319,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009303",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "9fbf40c9-fe4d-4c45-8ff3-6f2ac59949c8",
      "created": 1623571302002,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009120",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "2b38a3f3-7921-48b3-a596-4912c9132f3c",
      "created": 1623556925169,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009704",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "5ea92c3c-20b6-4211-a8b0-4d760bd37861",
      "created": 1623542513721,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009937",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000199
    },
    {
      "id": "0f70f1a1-874a-44c9-a84f-e8fc079717c3",
      "created": 1623528120196,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010681",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000214
    },
    {
      "id": "c54f8b8f-cc40-4bf2-b281-085b6bc8ab5f",
      "created": 1623513718877,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009905",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000198
    },
    {
      "id": "18fe490c-d1f5-4fd2-a981-e6a08d08f803",
      "created": 1623499390911,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007022",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000014
    },
    {
      "id": "547117b6-8ddc-4cb9-a024-ad65064ccf76",
      "created": 1623484949199,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009624",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "fde85354-92bb-4d6b-92f0-57ff2a8a8552",
      "created": 1623470551566,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009215",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "115c043b-2bba-4b41-87d2-7d63bcbf55e3",
      "created": 1623456127690,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009841",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "5f449ecc-c4a7-4a07-af42-16d74bb23e9a",
      "created": 1623441820696,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010558",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000211
    },
    {
      "id": "3795bc34-4ab0-4f83-a5e2-ad8d564dc9f7",
      "created": 1623427318491,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009438",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "91fd4188-0de2-48ad-9268-a3f9f65acf8c",
      "created": 1623412977381,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009334",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000187
    },
    {
      "id": "46bbd788-fdd8-4ea8-932a-1301e7db3ffe",
      "created": 1623398499432,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009592",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "261498b3-8f4e-426d-af5b-389a62ac8050",
      "created": 1623384128547,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009987",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "eb4ade2b-c87c-4ef4-84a9-0a33a8e2fb21",
      "created": 1623369693654,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009664",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "06b42e24-44b6-44a4-990a-54db5071a260",
      "created": 1623355467570,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010485",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "65cf5866-df5f-49e9-9b9c-bcf167570549",
      "created": 1623340920702,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010113",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "a16fb444-5812-4021-bdc2-110bf63ff23e",
      "created": 1623326519750,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010078",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "e1a35a99-efad-420b-ae4a-4df0cd15876b",
      "created": 1623312152231,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009995",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "4a5a75f8-f6ca-4a39-a446-c2f5684755e0",
      "created": 1623297736120,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009732",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "0dbb7eb7-f80f-4097-adda-e5d404da5356",
      "created": 1623283380722,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010286",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000206
    },
    {
      "id": "1ef75dc3-3aa3-4937-9a24-bc16d23d7ebe",
      "created": 1623268990016,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011630",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000233
    },
    {
      "id": "bbd9edd9-1060-4059-b8bb-f265a8826b5f",
      "created": 1623254580111,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010781",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "3fca0b0b-8b4e-4d59-8f27-11bf68d0d71f",
      "created": 1623240124976,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010059",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "4fa01321-b746-4b57-ad5d-4ad3d79d449e",
      "created": 1623225805595,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009378",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "d5edecec-0fb3-487a-ab11-a3513ade0cdd",
      "created": 1623211362571,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008725",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "c25631e0-a7fc-4962-9433-86e84df58aae",
      "created": 1623196942656,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011003",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "061ed3fd-9b44-4f23-8e13-cdf9b93ff330",
      "created": 1623182565772,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011752",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000235
    },
    {
      "id": "888bc339-551e-4a77-88c9-e417d0264eb9",
      "created": 1623168193182,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010744",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000215
    },
    {
      "id": "a48b254c-9e48-4c5a-9b07-8143abee27dd",
      "created": 1623153748241,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009619",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "316ca656-28df-4aec-bed7-a375cf652af5",
      "created": 1623139349719,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011304",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000226
    },
    {
      "id": "43402828-83fb-4a81-95de-f7d6742d2b66",
      "created": 1623124992042,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "3a2082ea-5fd8-4f35-a882-b954fd20fbac",
      "created": 1623110615621,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010405",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000208
    },
    {
      "id": "feb471c6-738a-4317-92dd-0b6ff8d9ccd6",
      "created": 1623096216699,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011936",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000239
    },
    {
      "id": "d86e245e-311d-421d-b373-1f73694eea1c",
      "created": 1623081815253,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010827",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000217
    },
    {
      "id": "f75d9f13-29d3-491f-9d36-0d8ab13566eb",
      "created": 1623067379902,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010594",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000212
    },
    {
      "id": "0445534f-d63f-4f48-8403-7bee2b7d8388",
      "created": 1623052918941,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010321",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000206
    },
    {
      "id": "f24797ad-f597-4619-88c2-d47081fe2c08",
      "created": 1623038515802,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010016",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "63a073af-44d8-4d93-b68f-789ae7a3160c",
      "created": 1623024150472,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010269",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "110fecca-5e4e-41a2-915f-19c0b1faa3b0",
      "created": 1623009717682,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009823",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "a7d7bb1d-6847-4994-8d93-97d3d20939cb",
      "created": 1622995331965,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007666",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000153
    },
    {
      "id": "ff5f408a-a2dd-4c98-944c-36dd5a3c19f6",
      "created": 1622981018581,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009443",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "92e59427-f8ad-4504-9542-2b55d596ec89",
      "created": 1622966636004,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010270",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "51c76fa9-201e-4f54-8786-ff70073e45ef",
      "created": 1622952110932,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010181",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "3da3db68-eca6-4be8-8285-e6f3ee3998b5",
      "created": 1622937725389,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010594",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000212
    },
    {
      "id": "b944e3f6-8b5a-4825-ab21-6f989902eeef",
      "created": 1622923431757,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010407",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000208
    },
    {
      "id": "04f880a4-c31e-4351-a559-ac780573b5cf",
      "created": 1622908986742,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010561",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000211
    },
    {
      "id": "658a720b-988c-407a-9704-6213d700f5f0",
      "created": 1622894531829,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010429",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000209
    },
    {
      "id": "5332b8c5-eb38-47dc-b047-df9efa32dad6",
      "created": 1622880191967,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010420",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000208
    },
    {
      "id": "720db87b-2f76-46c7-b639-6b6e8546d679",
      "created": 1622865777178,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010427",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000209
    },
    {
      "id": "8e7b67da-ed3c-4be0-a668-04151737e15f",
      "created": 1622851364079,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010492",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "f15db9a9-1572-4630-946c-92f2cf649cc1",
      "created": 1622837015795,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010755",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000215
    },
    {
      "id": "640e644a-f0f6-4923-9d76-122667f7749d",
      "created": 1622822536276,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009015",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "05b2bf6b-8049-4d91-a537-f398ab1dceac",
      "created": 1622808175324,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009407",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "34611051-36c2-40b9-81b9-9d0bff5480a2",
      "created": 1622793786686,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010854",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000217
    },
    {
      "id": "d7842832-02ef-4d00-89ae-969612a33c0c",
      "created": 1622779402005,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011370",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000227
    },
    {
      "id": "e7488669-8eb1-40bf-b3fe-5ac9c700dd26",
      "created": 1622764906140,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011568",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000231
    },
    {
      "id": "990a607c-e699-4fe6-b52e-411801eee1ca",
      "created": 1622750521205,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011291",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000226
    },
    {
      "id": "03aeb8b2-9656-4cd5-8e4b-f88155f9112c",
      "created": 1622736281835,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011441",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "d1c5096c-9a69-41f8-856a-f33544428e62",
      "created": 1622721779443,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011083",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000222
    },
    {
      "id": "1de12f1e-6e17-476b-82ed-b79b635c9fe3",
      "created": 1622707474886,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010875",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000218
    },
    {
      "id": "6f802ae4-6688-4fb0-a5b0-c01f5b166f3c",
      "created": 1622692931546,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010812",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "9112c888-b486-4683-8e6d-ed09df023074",
      "created": 1622678604427,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011140",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000223
    },
    {
      "id": "20fecb71-f25b-4fa0-962f-84448432b36f",
      "created": 1622664165872,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011875",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000238
    },
    {
      "id": "2f6701e8-e66c-46c7-bb68-e20a7366bb6b",
      "created": 1622649751094,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011319",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000226
    },
    {
      "id": "618ae4cc-b9e5-42d5-8c2c-6488551bb3e4",
      "created": 1622635571438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011006",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "68537af5-04e3-475e-ab90-bcf2523008a4",
      "created": 1622620950530,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011328",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000227
    },
    {
      "id": "9e603ba3-4e91-42c3-b682-9f3dabf56fba",
      "created": 1622606597150,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011431",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "623f929e-6f22-410a-b5be-083a29ad4f55",
      "created": 1622592165949,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011056",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000221
    },
    {
      "id": "1fa83a1c-8a22-4ed7-ace0-77fd50a97240",
      "created": 1622577795465,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011799",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000236
    },
    {
      "id": "2a4184c7-5a42-4bc2-96b2-d18850c7df43",
      "created": 1622563411372,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011704",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000234
    },
    {
      "id": "2b1f4ca2-39f7-465b-a96a-2df8e6f06772",
      "created": 1622548983298,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011318",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000226
    },
    {
      "id": "aad6991f-40ff-490e-9c0c-d1978de6af3b",
      "created": 1622534626007,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010894",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000218
    },
    {
      "id": "2a426900-18b7-4da4-9382-ca4bfd8e7e36",
      "created": 1622520118397,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010799",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000216
    },
    {
      "id": "232ff9c4-d933-4ba0-9097-e7e401a8209f",
      "created": 1622505719119,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011386",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000228
    },
    {
      "id": "22d44b38-9de0-46c9-8e9e-6537265859f0",
      "created": 1622491349103,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011732",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000235
    },
    {
      "id": "c5901b60-74be-49b4-bb47-bd39f1704ac6",
      "created": 1622476891687,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011467",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "61a46991-5d31-42f1-a708-55d8078b9ca5",
      "created": 1622462555506,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010106",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000202
    },
    {
      "id": "37e9cab2-f711-4f6b-92df-32a140a87058",
      "created": 1622448176835,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010318",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000206
    },
    {
      "id": "ba84d957-3bdd-43e7-abcd-4b310afdc3d7",
      "created": 1622433802236,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009673",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "c9001319-df1a-470b-92cc-9eb84600465c",
      "created": 1622419315743,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009546",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "5881ca31-b9b8-4b5e-a28b-82729428824f",
      "created": 1622404953328,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010499",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "470da902-1feb-45ca-8083-34d2c502b2b5",
      "created": 1622390654029,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010303",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000206
    },
    {
      "id": "24392552-921c-42f4-969a-24a8ef284f9d",
      "created": 1622376113956,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010580",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000212
    },
    {
      "id": "659a2ca7-772e-454c-b546-e728d4c2754f",
      "created": 1622361777632,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010326",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000207
    },
    {
      "id": "e4adf9fd-3022-4f75-928a-09325fe5bdb3",
      "created": 1622347393250,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010190",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "c03a26c7-9450-41b5-9a94-8390de2ade46",
      "created": 1622332942286,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010189",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "a5363b59-2123-4ad1-8734-ad7b010592a5",
      "created": 1622318507338,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011279",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000226
    },
    {
      "id": "ff6c9835-f999-4e4a-8114-91e512fda032",
      "created": 1622304129428,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010884",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000218
    },
    {
      "id": "ef0a3fc0-bc62-4cc9-a9b3-899c77ad082b",
      "created": 1622289699243,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011002",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "7405b94b-8ef2-4311-b097-3c2f067e0697",
      "created": 1622275382353,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011108",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000222
    },
    {
      "id": "2152bc67-14aa-4a14-85f0-e27792024ddc",
      "created": 1622261024898,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010741",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000215
    },
    {
      "id": "cffd4a21-09df-4f4c-ad2f-96b6f6200c47",
      "created": 1622246562230,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010991",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "1ad5b0b3-a04b-4906-88ca-d64a1e8957d8",
      "created": 1622232102112,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011689",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000234
    },
    {
      "id": "120194f5-6944-4d01-bff2-16812218b132",
      "created": 1622217764077,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011565",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000231
    },
    {
      "id": "308e7903-73eb-4bed-a454-8163f878b969",
      "created": 1622203453878,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011854",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000237
    },
    {
      "id": "7a0739bd-2a04-45a1-9956-85f0ef604d5e",
      "created": 1622189014164,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011800",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000236
    },
    {
      "id": "273cac0e-a36a-43e7-bb03-77586e585b41",
      "created": 1622174592054,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011345",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000227
    },
    {
      "id": "97e73070-be2d-4b38-9696-d3a453a39de2",
      "created": 1622160121812,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011792",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000236
    },
    {
      "id": "d37fbe6c-fdf9-4e98-a250-db48deb7ff7a",
      "created": 1622145763240,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011920",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000238
    },
    {
      "id": "77ed0641-54df-4491-9499-483995f0d410",
      "created": 1622131363087,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011923",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000238
    },
    {
      "id": "fda0e171-0613-40d2-b6fa-2ab3a34e2c7a",
      "created": 1622116963588,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011695",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000234
    },
    {
      "id": "d052a1dc-b89b-48fa-9eb7-ce0ffe86db4e",
      "created": 1622102579408,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011696",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000234
    },
    {
      "id": "3dd0dccc-5846-4588-95be-75ee79889925",
      "created": 1622088186605,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011835",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000237
    },
    {
      "id": "8d4a7e7a-5ca0-4f7e-ac32-f16700b7f1c1",
      "created": 1622073738744,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012172",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000243
    },
    {
      "id": "c6492bab-d9a3-4ecb-8c35-29c1597d11ff",
      "created": 1622059335583,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012604",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000252
    },
    {
      "id": "98be3d9e-f8dc-4aa7-8519-5c7bd0143de4",
      "created": 1622044911987,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011558",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000231
    },
    {
      "id": "af88db1d-2c01-4258-b387-a9cc69901219",
      "created": 1622030691058,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011441",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "4db8c18f-9b09-46b7-8969-96ca7820cfe5",
      "created": 1622016202042,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011803",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000236
    },
    {
      "id": "82d48b63-d5c9-422e-8900-cb2b19a6f1b1",
      "created": 1622001816589,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011913",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000238
    },
    {
      "id": "1bdb7560-765c-4d84-b41b-9434472dd91f",
      "created": 1621987394864,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011463",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "9d6799bf-acef-43f3-a1ad-51e033c67e3f",
      "created": 1621972996793,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011672",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000233
    },
    {
      "id": "de74af28-3564-4b9a-8085-3bf68fb9a5b3",
      "created": 1621958541422,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012129",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000243
    },
    {
      "id": "a0e5c395-41e3-468f-a02e-28747c421a3b",
      "created": 1621944311655,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011421",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000228
    },
    {
      "id": "57b58263-fd9b-435f-8bef-0ddc859dce01",
      "created": 1621929850721,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011815",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000236
    },
    {
      "id": "e9896fd6-683c-43cd-ba95-7883be65c514",
      "created": 1621915407995,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011592",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000232
    },
    {
      "id": "468f2332-726f-49c8-8b9e-cabb1bed10dd",
      "created": 1621900909482,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012344",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000247
    },
    {
      "id": "1fcfa148-06f5-4fe5-a9d2-b31c0f4095a1",
      "created": 1621886667123,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013682",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000274
    },
    {
      "id": "a2918467-1cfe-4b10-9b74-b20802df5976",
      "created": 1621872192799,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012770",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000255
    },
    {
      "id": "566aac7c-78e7-41b8-b8a7-24c4c3793f57",
      "created": 1621857828537,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011067",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000221
    },
    {
      "id": "89565ee2-b808-4434-8ffd-e7750844a40d",
      "created": 1621843342277,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010493",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000021
    },
    {
      "id": "387e53f2-da81-46a9-96f4-da443de4be80",
      "created": 1621828911390,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010623",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000212
    },
    {
      "id": "b3d79b1b-2c2b-4fe9-8fc1-10030a5191f8",
      "created": 1621814636360,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014013",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000028
    },
    {
      "id": "27f3e435-09e9-4693-baab-b5921e247161",
      "created": 1621800151363,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00020936",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000419
    },
    {
      "id": "f5a73113-145c-4692-89d6-a16c6bf9d4cf",
      "created": 1621785961088,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00018280",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000366
    },
    {
      "id": "d4f0f323-b241-400a-887d-b41070bf3af1",
      "created": 1621771421127,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013657",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000273
    },
    {
      "id": "b429f7f0-24ab-4051-b574-090e41550c0e",
      "created": 1621757002639,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009779",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "5615b009-d4c8-42df-bd3b-ad9521398123",
      "created": 1621742562907,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010023",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "ab22ec3a-305e-461d-984f-4f321ae92375",
      "created": 1621728370223,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010061",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "b2a2877b-5e89-4233-96f8-69e9ea4f40f4",
      "created": 1621713920215,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010563",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000211
    },
    {
      "id": "10c29260-0c0a-466b-8d9f-c02be408988a",
      "created": 1621699428478,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011386",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000228
    },
    {
      "id": "60275a9d-fe10-4d45-998a-bff1e039523a",
      "created": 1621685203992,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011577",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000232
    },
    {
      "id": "5efc1df4-4fba-4813-b153-acf5e73ce5aa",
      "created": 1621670753809,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012086",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000242
    },
    {
      "id": "64b2b96d-6dac-46a5-80ba-ea4d5cbbb88d",
      "created": 1621656187479,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011961",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000239
    },
    {
      "id": "1679951f-b064-48c5-b471-9e10dfc0e313",
      "created": 1621641946521,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00019662",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000393
    },
    {
      "id": "a23edab7-43ce-4575-9369-024c370d439a",
      "created": 1621627495888,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017043",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000341
    },
    {
      "id": "699a928d-0f51-4e70-966d-3fdacfd29926",
      "created": 1621613050865,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00016489",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000033
    },
    {
      "id": "f6af93b6-ac30-484b-a752-d23b6a9b76dc",
      "created": 1621598630672,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011778",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000236
    },
    {
      "id": "0f81a769-d75c-45b3-ad01-b97ce1775665",
      "created": 1621584324916,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011687",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000234
    },
    {
      "id": "9e028aff-0f3a-4cba-85b0-2778c858eb14",
      "created": 1621569831233,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011473",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000229
    },
    {
      "id": "0595dc81-1f82-4698-a90d-34d4c50e6a8b",
      "created": 1621555605846,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014286",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000286
    },
    {
      "id": "afab1b66-9e44-489e-9e79-9fde35bc677c",
      "created": 1621541129570,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014799",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000296
    },
    {
      "id": "1235c585-d559-43c8-9b8f-a3368afd71e1",
      "created": 1621526733348,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014310",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000286
    },
    {
      "id": "c3fedfec-7afd-42ac-9e3c-11caaf2e4be6",
      "created": 1621512267585,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012871",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000257
    },
    {
      "id": "db0a53d2-6473-4190-b80e-6369a8b6b209",
      "created": 1621497826275,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014075",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000282
    },
    {
      "id": "ff8e7411-bb4b-4c6c-9da7-b962527e3d9f",
      "created": 1621483371559,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017756",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000355
    },
    {
      "id": "d326beb5-1ac9-4f4e-853a-84606bfba33b",
      "created": 1621469037700,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00019006",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000038
    },
    {
      "id": "e6626604-a787-4778-9601-b0306a5df0b0",
      "created": 1621454641600,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00025643",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000513
    },
    {
      "id": "2e85f6ad-1a3b-4f9b-990d-48e2255a981b",
      "created": 1621440267940,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00046720",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000934
    },
    {
      "id": "1b39bc97-6eba-4ad6-836d-2148ad281e49",
      "created": 1621425838672,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017339",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000347
    },
    {
      "id": "7cc0e9b8-3223-43d4-b835-9c1522680366",
      "created": 1621411374348,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00021559",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000431
    },
    {
      "id": "94114965-f4e7-45f9-8a59-f4a302315439",
      "created": 1621397017692,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015227",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000305
    },
    {
      "id": "c3c5e7fe-a6ab-481c-9738-0abd8883a071",
      "created": 1621382558858,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015451",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000309
    },
    {
      "id": "f7e84c42-8dd3-47ae-a590-d08eb71a7072",
      "created": 1621368175283,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00016999",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000034
    },
    {
      "id": "b7d6c6bb-6797-440d-84db-7ca2a6a107e3",
      "created": 1621353966562,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000305
    },
    {
      "id": "88754e77-100c-4717-8580-a2696ba69138",
      "created": 1621339379362,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012995",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000026
    },
    {
      "id": "7a75418d-0af1-4dec-8c22-f565e6f8a7e0",
      "created": 1621324961222,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013868",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000277
    },
    {
      "id": "9601611b-2183-4ddb-8a99-9c3b666a22e2",
      "created": 1621310674186,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013712",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000274
    },
    {
      "id": "a31f4c81-78ab-459c-a7d6-5ae33df7532f",
      "created": 1621296228068,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014829",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000297
    },
    {
      "id": "cbd0d41c-6f49-4f68-b992-f6cbf38551ef",
      "created": 1621281853960,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017691",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000354
    },
    {
      "id": "e5503569-5546-4b78-bb84-633b3fe6b7db",
      "created": 1621267372116,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014479",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000029
    },
    {
      "id": "43afa901-2643-48b3-bc49-1c4cac048dcb",
      "created": 1621253107952,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014133",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000283
    },
    {
      "id": "f5467767-1977-4e25-8e5b-9bec21f20883",
      "created": 1621238598262,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015793",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000316
    },
    {
      "id": "108cb847-3a80-4311-b2b6-55fa05f1c7b6",
      "created": 1621224174907,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013626",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000273
    },
    {
      "id": "77cdcb36-7298-4051-8bcd-efc5fe6fe41f",
      "created": 1621209733656,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017629",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000353
    },
    {
      "id": "0927d25a-aaf9-4ffe-a93d-c03d0e7aad16",
      "created": 1621195354398,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015033",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000301
    },
    {
      "id": "e955f65f-5b25-4758-afe1-36ac10b47c85",
      "created": 1621180952344,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012342",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000247
    },
    {
      "id": "d4366bff-a263-47c2-a97b-a3cfecc2a1d0",
      "created": 1621166544956,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009710",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000194
    },
    {
      "id": "56ad08b4-357d-4686-b47c-0db492b2b3af",
      "created": 1621152152003,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009193",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "9fe956f8-bcec-4141-908d-545ce1db106c",
      "created": 1621137741871,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012084",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000242
    },
    {
      "id": "d33d235a-41aa-403b-963f-b76c1d5668cd",
      "created": 1621123354468,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014719",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000294
    },
    {
      "id": "f527e57a-757a-40f9-ba2d-1f6789071263",
      "created": 1621108949440,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00016170",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000323
    },
    {
      "id": "c6eaa1a2-163d-4ae4-8c2e-6ba07f5d63b8",
      "created": 1621094672471,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00016310",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000326
    },
    {
      "id": "b9bac173-9d79-4e84-8cd9-191e714fdd1c",
      "created": 1621080183214,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00016603",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000332
    },
    {
      "id": "5384c704-9f0e-487f-83f1-818cddf11b97",
      "created": 1621065747625,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017209",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000344
    },
    {
      "id": "293829ee-0e22-4fdc-a918-771a972efe89",
      "created": 1621051345178,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017596",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000352
    },
    {
      "id": "ce356718-53bc-469f-95a6-18a1377afbc1",
      "created": 1621036940626,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00018816",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000376
    },
    {
      "id": "7930085a-68ee-4b44-8520-42bfce01034f",
      "created": 1621022572491,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00020418",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000408
    },
    {
      "id": "89a9fe92-aec3-4667-9b2b-77ac3dc4d84b",
      "created": 1621008192190,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00019804",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000396
    },
    {
      "id": "43f34b3c-f6eb-415a-8fd8-e5bb4ea745aa",
      "created": 1620993763179,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015635",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000313
    },
    {
      "id": "48cab182-18bd-4912-a29d-c9f3c17996b2",
      "created": 1620979436663,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015616",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000312
    },
    {
      "id": "29e58858-b334-4c85-9f86-ac77cf567a24",
      "created": 1620964975276,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015772",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000315
    },
    {
      "id": "0673b63f-2448-4bed-abf2-bbb68953d617",
      "created": 1620950619442,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017588",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000352
    },
    {
      "id": "f4226024-1fc3-4b14-8e13-ca514ed8ad5d",
      "created": 1620936253544,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00019856",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000397
    },
    {
      "id": "b95acfb3-3c8b-4108-962c-0f34ed3f7c22",
      "created": 1620921710754,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00020546",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000411
    },
    {
      "id": "87d7b79d-66f4-42bb-bf02-ed1860b23be4",
      "created": 1620907554732,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00020856",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000417
    },
    {
      "id": "523cac37-7465-46ac-933c-b37fd0c236d3",
      "created": 1620892965657,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00020386",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000408
    },
    {
      "id": "03db457a-5ea1-47d9-928f-42247cba2956",
      "created": 1620878639910,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00027178",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000544
    },
    {
      "id": "6a3c565b-50eb-45b6-abd8-7ba7ca544b7c",
      "created": 1620864364201,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00025721",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000514
    },
    {
      "id": "de2aa508-a528-469a-bfb1-f60198e4cd52",
      "created": 1620849829991,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00037854",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000757
    },
    {
      "id": "90405d01-e152-46f7-86f6-88401c3b2293",
      "created": 1620835490612,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00027021",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000054
    },
    {
      "id": "fa6acb9e-0f68-4477-b138-ad2e65cdb570",
      "created": 1620822127750,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00021427",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000429
    },
    {
      "id": "ffe41add-f3b8-4293-a0be-3d34cb0da5b2",
      "created": 1620806626513,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00024270",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000485
    },
    {
      "id": "046179aa-7b32-459e-8f55-9bb79540c3bc",
      "created": 1620792321218,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00024679",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000494
    },
    {
      "id": "58fcabae-4eb9-4d0f-b7f7-2239200f4ade",
      "created": 1620777805760,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00020077",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000402
    },
    {
      "id": "3b7c5792-9293-497f-bbe6-0cccd7cf3b51",
      "created": 1620763476052,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00025660",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000513
    },
    {
      "id": "36ecc8c9-b525-4caf-b673-cb3ee86fc7ea",
      "created": 1620749081983,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00030593",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000612
    },
    {
      "id": "f38c1dd0-48e5-4a69-920d-6d456573467a",
      "created": 1620736521611,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00023052",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000461
    },
    {
      "id": "4c770a88-ea45-4a74-a61d-eece37396e17",
      "created": 1620720000000,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00019130",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000383
    },
    {
      "id": "35b27ceb-cc1b-47d4-8d3c-345b0ad23b3d",
      "created": 1620706113662,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00023165",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000463
    },
    {
      "id": "e5d48a6f-f81d-4007-9299-9bdd2fa4b6f2",
      "created": 1620692655381,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00024953",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000499
    },
    {
      "id": "2e1cac70-7a03-428c-b2e1-f1d9967df3ac",
      "created": 1620677520367,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00025159",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000503
    },
    {
      "id": "a6dc6a03-b2f4-4f50-92b9-1e758ae71a77",
      "created": 1620663261134,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00030704",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000614
    },
    {
      "id": "3faa031c-f8c8-4d4c-9fae-632303478217",
      "created": 1620648343441,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00019499",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000039
    },
    {
      "id": "5862b9bc-5cb8-4e32-8f38-2f22ab251464",
      "created": 1620634001625,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015567",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000311
    },
    {
      "id": "8c8d3fdf-2c67-496c-9771-56cd82afaaac",
      "created": 1620619674727,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00015074",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000301
    },
    {
      "id": "4de78883-e74a-48ab-b27a-b25762461334",
      "created": 1620605353555,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014511",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000029
    },
    {
      "id": "c2589696-4539-4ae7-8643-e7812920c095",
      "created": 1620590983567,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013764",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000275
    },
    {
      "id": "794f7953-4402-4537-aecd-6d6e6c64c8f5",
      "created": 1620576457623,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014693",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000294
    },
    {
      "id": "9f3a6539-155b-41a0-a19a-f3698193a453",
      "created": 1620562087484,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014943",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000299
    },
    {
      "id": "ce162133-7a55-4107-896c-00a5b18b3939",
      "created": 1620547740346,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013109",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000262
    },
    {
      "id": "16b0ca53-e5d9-4d01-8927-53f3b92f1ef0",
      "created": 1620533058716,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00016757",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000335
    },
    {
      "id": "f4411bbc-5509-482c-a144-0ff3d5e2df0e",
      "created": 1620518972391,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00017496",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000035
    },
    {
      "id": "0b527e50-9ea3-4f41-a1fb-5c39d2388472",
      "created": 1620504590993,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00021438",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000429
    },
    {
      "id": "adf69591-dd1b-488d-a547-4c6fb8c46736",
      "created": 1620490163999,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00014260",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000285
    },
    {
      "id": "dd3382aa-e993-4405-ae7d-f0125681dbcf",
      "created": 1620475475752,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012729",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000255
    },
    {
      "id": "55ad5b0c-f4fd-4977-85a5-cc91cb3efbd3",
      "created": 1620460985762,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010703",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000214
    },
    {
      "id": "f1296602-8927-4258-9bd3-c07064ca9961",
      "created": 1620446864709,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006160",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000123
    },
    {
      "id": "6eba2c4b-6175-4cc2-8fd5-d197b2329e32",
      "created": 1620432365119,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010752",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000215
    },
    {
      "id": "f44a3906-823c-4b89-9147-fed873c42f51",
      "created": 1620417897022,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013170",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000263
    },
    {
      "id": "5fe2ac02-990e-4b9d-ad71-b50ca9b41de7",
      "created": 1620403658254,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012055",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000241
    },
    {
      "id": "2c7ec59f-68b4-47eb-894e-8ed0edf16582",
      "created": 1620389107421,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010686",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000214
    },
    {
      "id": "841145e0-2b5b-45a4-bbe1-6fa3e3538923",
      "created": 1620374914680,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010563",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000211
    },
    {
      "id": "3947fdd2-88eb-490b-85d7-19371de8cece",
      "created": 1620360389824,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011174",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000223
    },
    {
      "id": "de0db32a-6fd7-4420-830e-e87e8d8742c4",
      "created": 1620345865412,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011556",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000231
    },
    {
      "id": "5ac5a22c-8e8a-45cc-9f9f-85a6096002b8",
      "created": 1620331519324,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012584",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000252
    },
    {
      "id": "e884efa1-6f04-4ae2-b70a-8db5d7b8ad09",
      "created": 1620317121626,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010967",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000219
    },
    {
      "id": "0b6c865b-7bb7-4e46-8373-417fe13db5c5",
      "created": 1620302969412,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010225",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "4df767f6-c8b4-480c-a153-10d7bc3f5561",
      "created": 1620288604515,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010251",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "8bbd5e07-8480-4106-82c2-6a2fe5080cda",
      "created": 1620273966856,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011026",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000221
    },
    {
      "id": "1096e417-6e96-4fc4-8237-48e248123269",
      "created": 1620259464714,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011872",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000237
    },
    {
      "id": "b215fb11-e870-4ad4-be08-2645a57a077c",
      "created": 1620245118310,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012160",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000243
    },
    {
      "id": "7085b247-bfdd-47a0-ada6-8203d6fd3d65",
      "created": 1620230709212,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011689",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000234
    },
    {
      "id": "6cc153d7-bd57-4639-8563-80053178cb5c",
      "created": 1620216398652,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010065",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "1325c29f-d2cd-481b-8316-8f96eaf8de06",
      "created": 1620201981934,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010583",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000212
    },
    {
      "id": "556a2684-ac0d-4433-8e1e-f5d64a1d0d96",
      "created": 1620187560734,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011716",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000234
    },
    {
      "id": "e1e71a2f-d710-4193-8348-5acb37e58bc6",
      "created": 1620172938302,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012198",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000244
    },
    {
      "id": "42586baa-d0d6-4d76-8f1c-aabfe2f54c1f",
      "created": 1620158844160,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00013725",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000275
    },
    {
      "id": "c8e8a6f8-c635-4bf2-b181-0e68574c7155",
      "created": 1620144766738,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012095",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000242
    },
    {
      "id": "a63aa194-7444-40ba-a16d-6ce19082eb35",
      "created": 1620129932399,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002380",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.8e-7
    },
    {
      "id": "72f62742-78fc-481e-a7bb-6eb214994989",
      "created": 1620125589867,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005395",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000108
    },
    {
      "id": "633fd86b-7868-46e9-b2cf-020980c607e4",
      "created": 1620101370231,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011643",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000233
    },
    {
      "id": "d654e12c-f056-49dd-a9c0-e65b1adbfadf",
      "created": 1620086649335,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012487",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000025
    },
    {
      "id": "d8ffe8ac-1a02-4777-b066-b5c6b9a94b1a",
      "created": 1620072341455,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00012640",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000253
    },
    {
      "id": "7dc043ce-eeee-4051-bf6e-43109f90b88d",
      "created": 1620057938471,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009823",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "479cb8a5-907c-4f99-9851-b17f30883eb4",
      "created": 1620043525420,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009498",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000019
    },
    {
      "id": "80c036d3-eed2-4772-bdae-c5517aef4afc",
      "created": 1620029112427,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008909",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "f0964592-7f02-40d1-a112-092687a33c9a",
      "created": 1620014762829,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008937",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "3767dfa6-7950-4062-98e5-325530975324",
      "created": 1620000243802,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009596",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000192
    },
    {
      "id": "b3e1902f-29a1-4df8-9c84-53765c82fcb4",
      "created": 1619985910516,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009472",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "a0f54219-8e33-4d7d-b762-a09314348077",
      "created": 1619971497702,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008777",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "450bf263-db65-4b6c-99c1-815958f98248",
      "created": 1619957115568,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008704",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "523e933f-ab0a-47cf-a465-e5f303276c34",
      "created": 1619942869785,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008786",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "180d06d6-3825-4851-80b9-1c5d85eb3b37",
      "created": 1619928234405,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009150",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000183
    },
    {
      "id": "7d6db227-7eb5-47a0-8f2f-41d60eef4aea",
      "created": 1619914086612,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009631",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000193
    },
    {
      "id": "0c68cb48-f502-45a7-9fd5-1c692fe6cb39",
      "created": 1619899597198,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009449",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000189
    },
    {
      "id": "51e6cdf9-1f81-45b0-ba60-4e66818984c2",
      "created": 1619885209094,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008670",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000173
    },
    {
      "id": "94948268-ac31-4319-972e-557be801a9d0",
      "created": 1619870871004,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009046",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000181
    },
    {
      "id": "908a8d6d-bb15-426f-9efa-d284433054bc",
      "created": 1619856466360,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008772",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "d8707f48-7aa3-4d13-a3ad-37c661c7b1cd",
      "created": 1619841840226,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007144",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "468a433b-d294-42f0-872c-39d459bef627",
      "created": 1619827489195,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006972",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000139
    },
    {
      "id": "1d84f757-6c2d-4ef6-a52e-552385f21f3b",
      "created": 1619813436393,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009737",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "d8414314-fd0c-41a6-a3b2-b73a94e7292c",
      "created": 1619798908115,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009988",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.000002
    },
    {
      "id": "5b0b4fb9-8617-4460-a7ed-29ccdbbab0b3",
      "created": 1619784476061,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009403",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "274a013b-8e59-4f3a-9892-dccd70046407",
      "created": 1619769837013,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009023",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000018
    },
    {
      "id": "039a1e56-3cce-4b59-9df5-07f3cdedb9fa",
      "created": 1619755465750,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009263",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000185
    },
    {
      "id": "8c3f2a61-33f1-4c37-8749-122ddb86280a",
      "created": 1619741029244,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009835",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "f9cc034d-2dd5-4f9e-9ebf-2b7292146411",
      "created": 1619726639028,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011537",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000231
    },
    {
      "id": "ee00b7c4-52e1-4eda-90b7-5f7b1eb22da8",
      "created": 1619712302648,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011246",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000225
    },
    {
      "id": "1c1a93fd-eba0-4389-9f96-bd0756e72fd8",
      "created": 1619698012679,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010263",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000205
    },
    {
      "id": "c851d339-85dd-4d07-960c-4ce006dd01c0",
      "created": 1619683358742,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009738",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000195
    },
    {
      "id": "b1220701-9001-47a9-9672-6934cdccce5c",
      "created": 1619669023901,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009394",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "a5d170ce-4329-4b5c-b500-3e8254c9e0d3",
      "created": 1619654753830,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009868",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "85399345-0b60-4402-bd23-a418cdf79430",
      "created": 1619640236954,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010639",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000213
    },
    {
      "id": "0077241e-8454-446c-b958-49a11e268db3",
      "created": 1619625917002,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010706",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000214
    },
    {
      "id": "89e84448-2960-46af-93de-af7adfeb9480",
      "created": 1619611562766,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008806",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "e7ed41c6-bc2a-46f8-bda5-e91ec5534022",
      "created": 1619597086796,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008910",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "df29cf6b-5afa-4b09-ba65-ff4d286ce7c0",
      "created": 1619582552342,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008546",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "919c90cc-906c-4e00-8a89-bd017fa27960",
      "created": 1619568247063,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009180",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000184
    },
    {
      "id": "2dd9b5a4-126e-4082-80ea-624666f2811f",
      "created": 1619553941674,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009853",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "ca9e31c8-32e3-4910-9f4d-846af70aa16f",
      "created": 1619539635594,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009322",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000186
    },
    {
      "id": "9222643a-8a00-4bf2-be2d-f632b1ec72ab",
      "created": 1619525157947,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008734",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000175
    },
    {
      "id": "2bf663e1-7f70-49de-8785-9d174a64c7e5",
      "created": 1619510703744,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008930",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000179
    },
    {
      "id": "d631d0ce-2fc5-4689-83d0-cc7971c807bb",
      "created": 1619496103444,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008325",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "a650c5f8-94cd-4f42-83ad-2450497f99b9",
      "created": 1619481856189,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008706",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "830b8b17-bafe-41f9-a1b7-0a119d0514b1",
      "created": 1619467495798,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008221",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "c6ff9215-6e58-4f47-820a-a57ae36e2656",
      "created": 1619453117001,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008239",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "d4d0dca8-d2a9-42aa-8154-0996b1dbf04b",
      "created": 1619438575706,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008696",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "e4be1c15-b270-4f79-9b7a-f2979f18f6fb",
      "created": 1619424317118,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008778",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "04d5edff-a163-4400-ad0b-49efb3cd8ab0",
      "created": 1619409914436,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008453",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "07845527-51a0-4250-9538-531c0f14ec57",
      "created": 1619395317735,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008822",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000176
    },
    {
      "id": "1ce78a8d-c52c-45fa-a99d-f25beca1224a",
      "created": 1619380950717,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008352",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "e538d437-9b59-44ba-ba2e-4afa3998439d",
      "created": 1619366521240,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008449",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000169
    },
    {
      "id": "535bac1c-d808-4cb2-b974-5ad20d677f1a",
      "created": 1619352152685,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008162",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "ce302025-5b30-4ebf-a4c0-37d37b5ec4fb",
      "created": 1619337781724,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008294",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000166
    },
    {
      "id": "941df194-89c6-4c9a-9928-c6342ac0dc01",
      "created": 1619323259244,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006416",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000128
    },
    {
      "id": "032bcf38-ffbf-4fd3-9fe4-ce8d93c5034e",
      "created": 1619308901363,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008223",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000164
    },
    {
      "id": "5b61308a-4524-42aa-83c2-60d20bab7ff2",
      "created": 1619294536454,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008230",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000165
    },
    {
      "id": "c6fb49ab-1d5a-4822-8a76-981749a84ad6",
      "created": 1619280195389,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004852",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.7e-7
    },
    {
      "id": "42b32f8b-d50b-4ec4-b341-8038dab11451",
      "created": 1619265771564,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006420",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000128
    },
    {
      "id": "a77abdf6-099d-4700-8c81-97f8321b8cd1",
      "created": 1619251365612,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008548",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000171
    },
    {
      "id": "3c053d9f-812d-442d-aa01-dad0f8a018ca",
      "created": 1619236998824,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009386",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000188
    },
    {
      "id": "fb59fdd5-1231-4732-8c83-526764749f0a",
      "created": 1619222517942,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008898",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000178
    },
    {
      "id": "89fcb399-476e-4b23-b68c-b615f05d0871",
      "created": 1619208023774,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008125",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000163
    },
    {
      "id": "5992fef0-3f7e-4d54-ac08-fc312e2edd29",
      "created": 1619193701603,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010217",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000204
    },
    {
      "id": "d1fe0278-d24b-4664-b079-151279e0e8cd",
      "created": 1619179341438,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010046",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000201
    },
    {
      "id": "b9fd941e-5617-484c-98ee-e9a99d4cf0a8",
      "created": 1619165137335,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010635",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000213
    },
    {
      "id": "3f42abe7-3d8c-4422-97c3-0bfc794ed02c",
      "created": 1619150511794,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010319",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000206
    },
    {
      "id": "328963a7-288b-4f90-a21f-9c6930a1bb6b",
      "created": 1619136054074,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008399",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000168
    },
    {
      "id": "36299f74-dd42-4c36-a635-1cc0e9d40f14",
      "created": 1619121801788,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010981",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000022
    },
    {
      "id": "6cc7414c-5aaf-4766-b21a-ee17d7241e3d",
      "created": 1619107280673,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010946",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000219
    },
    {
      "id": "4503cdfc-ba69-469f-8ebc-5d3b9b064548",
      "created": 1619092919906,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007142",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "39d5392c-2e15-46b3-9c37-697bec12397f",
      "created": 1619078461657,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007441",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000149
    },
    {
      "id": "364928dc-f928-4f86-b4af-9d0426df7b2f",
      "created": 1619064196116,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008105",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000162
    },
    {
      "id": "c4608b5a-71dd-4e9b-a0bf-736d010862fa",
      "created": 1619049695305,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009857",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000197
    },
    {
      "id": "9c7011e4-ee2a-4f88-8951-191915efe0d6",
      "created": 1619035546933,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009075",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000182
    },
    {
      "id": "5795c07a-1d39-45e3-8949-4bd3534c99a8",
      "created": 1619020854445,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008493",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.0000017
    },
    {
      "id": "67bb524e-4abf-45ed-9178-4420072379aa",
      "created": 1619006434910,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005823",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000116
    },
    {
      "id": "a3087917-8f6f-4e5c-aba9-a79aa473de3a",
      "created": 1618994581014,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007141",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "9d35618e-7e0a-47b6-b6d0-5702093616b8",
      "created": 1618963475326,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00011619",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000232
    },
    {
      "id": "157084fc-1344-4490-97b5-31259998801e",
      "created": 1618949152990,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010918",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000218
    },
    {
      "id": "e6d53319-19ef-4671-8328-e850cbf22d4d",
      "created": 1618934424069,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009806",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000196
    },
    {
      "id": "0251c719-be7a-4505-b218-9a4f7e0b050e",
      "created": 1618920752823,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00010448",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000209
    },
    {
      "id": "f8f7cc2d-3bad-40b2-ae3f-90e9f8ced8f7",
      "created": 1618905726272,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008697",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000174
    },
    {
      "id": "eb733718-71aa-4119-b9d8-78a47744a930",
      "created": 1618891286936,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00009552",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000191
    },
    {
      "id": "1addcc86-ef77-4d31-9add-36f0aaa9fb1a",
      "created": 1618877134416,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00008360",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000167
    },
    {
      "id": "f67dc59b-dff8-4af0-8742-9cbda02b4745",
      "created": 1618862823973,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006725",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000135
    },
    {
      "id": "48151dfc-9794-43e8-81e9-9bb710b9fa07",
      "created": 1618848105389,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00006676",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000134
    },
    {
      "id": "a710fc20-64da-4510-afb2-083d1cfe9c7d",
      "created": 1618833902469,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000119
    },
    {
      "id": "a6b19cde-d0ee-4378-91b5-5d2fe2ac6076",
      "created": 1618819630409,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004349",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.7e-7
    },
    {
      "id": "8cd5aa2a-2119-45d9-9b44-a2d1f6a335c6",
      "created": 1618805067184,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005074",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000101
    },
    {
      "id": "3550cf92-80ef-4201-96d5-95f1607dc5c9",
      "created": 1618790708468,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005727",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000115
    },
    {
      "id": "35de6b6f-ab40-40a0-be7b-8d3fae634d0a",
      "created": 1618776325307,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005679",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000114
    },
    {
      "id": "ca4d47d8-6178-4c0d-9b60-450af52f828b",
      "created": 1618761834176,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005655",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000113
    },
    {
      "id": "5092b1d8-9b65-42ac-b556-6dd5a78d62bd",
      "created": 1618747502361,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005704",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000114
    },
    {
      "id": "66db13ae-1759-4772-8875-3ff20a292352",
      "created": 1618733215715,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007214",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000144
    },
    {
      "id": "ff72499c-d307-4aac-b6a7-84e719b1d815",
      "created": 1618718691530,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005234",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000105
    },
    {
      "id": "2b0b581a-9ae4-4865-94e0-c424cceef626",
      "created": 1618704276612,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005271",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000105
    },
    {
      "id": "2abd19e4-5aa5-414a-a607-f905f31d87fc",
      "created": 1618689946192,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005703",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000114
    },
    {
      "id": "8d7dfade-3f40-453c-a737-0da64b240788",
      "created": 1618675509631,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005716",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000114
    },
    {
      "id": "7fe00b29-91ed-47c0-9aea-daa97492a29e",
      "created": 1618661185113,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005473",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000109
    },
    {
      "id": "b484ca98-ed88-492a-bde2-b2a0d61db5bb",
      "created": 1618646807822,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005451",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000109
    },
    {
      "id": "9b090818-bd2e-4ec6-9a01-69787922abba",
      "created": 1618632290094,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005247",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000105
    },
    {
      "id": "cee827d1-d651-4c73-a031-860355b0186b",
      "created": 1618617852019,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005965",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000119
    },
    {
      "id": "c2ea454b-9dd1-4cdc-9c0f-5baaed9835c0",
      "created": 1618603491513,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007129",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000143
    },
    {
      "id": "ea6f1d5c-4322-4bd9-84da-c54c3ff8d33c",
      "created": 1618589187769,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00007730",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000155
    },
    {
      "id": "ab1bc3ed-9062-47fb-af35-bc686105f957",
      "created": 1618574734722,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005328",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000107
    },
    {
      "id": "e07148ab-6965-4827-bf68-91d1ec96a498",
      "created": 1618560447740,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005266",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000105
    },
    {
      "id": "7f85b015-88a8-4847-9e66-99f9a228a278",
      "created": 1618545859601,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004865",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.7e-7
    },
    {
      "id": "1f554b03-2e7c-478d-8dc6-03d0eac53088",
      "created": 1618531427780,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004566",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.1e-7
    },
    {
      "id": "48e3e62c-fbde-4705-bc6b-55fc072dca09",
      "created": 1618517265574,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001923",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "a6877ae7-1325-4367-be75-a09123047f5f",
      "created": 1618502937726,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003830",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.7e-7
    },
    {
      "id": "9b753350-7b9a-42f5-af89-a6ced20fca27",
      "created": 1618488610183,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004445",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.9e-7
    },
    {
      "id": "620872ea-b64b-4967-b935-f1e2ebcb59b3",
      "created": 1618473951559,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004727",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.5e-7
    },
    {
      "id": "0549ee07-8841-4e86-bc45-61ba7f5e282d",
      "created": 1618459575759,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004529",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.1e-7
    },
    {
      "id": "d580660b-f57b-4f3b-a49a-673f9e508328",
      "created": 1618445262837,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004678",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.4e-7
    },
    {
      "id": "58a256cb-9810-4c62-8f34-b55950051331",
      "created": 1618430919941,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004735",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.5e-7
    },
    {
      "id": "fd62f5c8-d32b-465e-9822-8c41182b6208",
      "created": 1618416377753,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004764",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.5e-7
    },
    {
      "id": "8eab4bfa-f451-4e6c-836e-51d86f8ee77f",
      "created": 1618402027362,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004487",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9e-7
    },
    {
      "id": "a27bd9c5-32d7-442c-a56a-25bdb02b1880",
      "created": 1618387548995,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004308",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.6e-7
    },
    {
      "id": "58012438-c496-45d1-91ab-fb69573f9c7d",
      "created": 1618373218986,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004321",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.6e-7
    },
    {
      "id": "8352cce0-2d45-43c0-b177-685895e4f5fc",
      "created": 1618358680395,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004181",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.4e-7
    },
    {
      "id": "71006461-f0f2-444b-b223-795d7f6816dc",
      "created": 1618344322987,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00005146",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 0.00000103
    },
    {
      "id": "3aae5cd7-dddb-4326-b703-5ddeffac045e",
      "created": 1618329894763,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004442",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.9e-7
    },
    {
      "id": "7c7dc4e9-d4b0-40b9-beb4-f6c335aecf2e",
      "created": 1618315670599,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004144",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.3e-7
    },
    {
      "id": "696cd1cc-fd22-4abb-b95e-6d104986da3e",
      "created": 1618301242514,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003856",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.7e-7
    },
    {
      "id": "4debb77f-5b5d-4153-96de-79e5c0ef0b4b",
      "created": 1618286688439,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003048",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.1e-7
    },
    {
      "id": "0bdf9c09-96e6-4f34-b199-683847c72654",
      "created": 1618272406690,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003402",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.8e-7
    },
    {
      "id": "e3c2c5de-f4b1-419a-bd65-996397868640",
      "created": 1618258761932,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003964",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.9e-7
    },
    {
      "id": "1faf9b96-3435-46d7-a750-488ff358ce64",
      "created": 1618243784763,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003391",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.8e-7
    },
    {
      "id": "28748a34-b1f6-4b4e-90ad-8272c9d76a22",
      "created": 1618229569280,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003211",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.4e-7
    },
    {
      "id": "99a5f076-105e-4519-b2af-83a45d59b831",
      "created": 1618214823991,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003160",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.3e-7
    },
    {
      "id": "7a6de282-edc3-494f-9997-cca665dd3e82",
      "created": 1618200349937,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003056",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.1e-7
    },
    {
      "id": "43a57963-d188-41bd-a4da-52b6dcba55ef",
      "created": 1618186232471,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003397",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.8e-7
    },
    {
      "id": "49764848-5869-43cb-b40a-8d1919c8cb27",
      "created": 1618171743017,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003602",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.2e-7
    },
    {
      "id": "abee6e84-ad28-4b97-8a24-42d3db7f0f5d",
      "created": 1618157571059,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003443",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.9e-7
    },
    {
      "id": "b5cd3ac5-a70a-42ee-8f18-d3ae47b39947",
      "created": 1618143081995,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003501",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7e-7
    },
    {
      "id": "9e2118fc-fefe-4530-8cb9-5e72ae0b4a94",
      "created": 1618128460319,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003272",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.5e-7
    },
    {
      "id": "3b225293-307c-4a7c-9e1b-4409ca049688",
      "created": 1618114210781,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003324",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.6e-7
    },
    {
      "id": "fd212de0-6bb8-412c-a1dc-c7261877e2b6",
      "created": 1618099833240,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003354",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.7e-7
    },
    {
      "id": "35e2a476-3316-495d-a1a7-f2b14f9ee08f",
      "created": 1618085555371,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003728",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.5e-7
    },
    {
      "id": "f7477e88-057c-4315-9014-54d2980f068b",
      "created": 1618071352788,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003483",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7e-7
    },
    {
      "id": "42cd63e3-bec0-4bf6-90b3-5d95ce6a1038",
      "created": 1618056346097,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003674",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.3e-7
    },
    {
      "id": "4a35ea2d-0f32-4413-a503-7fcb30a7bbce",
      "created": 1618042319439,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003762",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.5e-7
    },
    {
      "id": "88fb2d29-1a46-4f8c-b3e3-6e4e4e1566da",
      "created": 1618027801935,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003669",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.3e-7
    },
    {
      "id": "6bccc7ca-e90f-420c-b86e-3ff36f16d30d",
      "created": 1618013459443,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003674",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.3e-7
    },
    {
      "id": "2ce32f84-62be-4ae0-b06c-44fc934c8ca9",
      "created": 1617999190915,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003776",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.6e-7
    },
    {
      "id": "8aa56514-b2ad-4d72-83e9-79b622665f74",
      "created": 1617984679568,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004213",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.4e-7
    },
    {
      "id": "e7e9686c-12e8-4d0b-a76b-5ced83fdcc58",
      "created": 1617970163617,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003628",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.3e-7
    },
    {
      "id": "dfa01d3b-3f0b-4f8b-b326-66571a5c1322",
      "created": 1617955697882,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003427",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.9e-7
    },
    {
      "id": "52efe82e-40a4-47bf-8c66-32fa08cd4d15",
      "created": 1617941047218,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003509",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7e-7
    },
    {
      "id": "419b2b09-a7c4-4dd7-a5b9-5f1dbdccdd06",
      "created": 1617926799813,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003645",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.3e-7
    },
    {
      "id": "f4a3e1e9-4e75-4996-a44a-f418db3e7679",
      "created": 1617912282475,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003914",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.8e-7
    },
    {
      "id": "ff54cc5a-1af5-476d-8073-0a8cd91c0787",
      "created": 1617898157908,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003782",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.6e-7
    },
    {
      "id": "d3bc8915-aefa-4067-9124-d325debacdd4",
      "created": 1617883921208,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003808",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.6e-7
    },
    {
      "id": "82f5e82b-c77f-421a-8a22-5c3040731104",
      "created": 1617869124083,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003759",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.5e-7
    },
    {
      "id": "de9ecbdc-39ed-4e80-8e9d-2a72168b50ea",
      "created": 1617854711025,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003839",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.7e-7
    },
    {
      "id": "f73bf908-953f-42db-8370-b37b24ebb14a",
      "created": 1617840354867,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004184",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.4e-7
    },
    {
      "id": "010fd7b8-2fcd-49ff-be25-0600c194ed38",
      "created": 1617825945955,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004196",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 8.4e-7
    },
    {
      "id": "5fa21cc4-1a1f-48ae-9caa-fcaa099aeaad",
      "created": 1617811469558,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00004528",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 9.1e-7
    },
    {
      "id": "7fdf5471-7c45-43d3-93ce-7feae1a38de6",
      "created": 1617797323835,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003956",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.9e-7
    },
    {
      "id": "7cef0b5a-84bf-4ca7-8773-61a81369ab89",
      "created": 1617782758312,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003811",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.6e-7
    },
    {
      "id": "164f2d0b-4fe1-4f0f-a28d-204c6640fb9d",
      "created": 1617768220444,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003877",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.8e-7
    },
    {
      "id": "0ba7c2e1-b654-4e5b-a862-d46d7ed82e24",
      "created": 1617753855285,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003150",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.3e-7
    },
    {
      "id": "da78aaf3-bbcb-46e8-bbcb-01fe778dd6df",
      "created": 1617739590648,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003856",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.7e-7
    },
    {
      "id": "b616dab5-eb05-4a73-b975-55b93fc129d5",
      "created": 1617725549032,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003696",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.4e-7
    },
    {
      "id": "f5d48fa8-f4d0-487c-9308-001d7a39ad9d",
      "created": 1617711009124,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003373",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.7e-7
    },
    {
      "id": "1a2ea914-af5a-4a7a-98de-dda98e6e2ea6",
      "created": 1617696305260,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003399",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.8e-7
    },
    {
      "id": "6faea6f5-6753-4403-ae52-afc6883e13b0",
      "created": 1617681928477,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003516",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7e-7
    },
    {
      "id": "e8880315-53df-432b-956c-09c4d096eb68",
      "created": 1617667462791,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003621",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.2e-7
    },
    {
      "id": "5b39f5cb-ee54-4ebd-8bbb-4e58c4ba87c4",
      "created": 1617653202597,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003954",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.9e-7
    },
    {
      "id": "7c56298c-afc6-4b39-be07-0832e6a6dbfb",
      "created": 1617638918684,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003712",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 7.4e-7
    },
    {
      "id": "e04cab19-bad6-414d-ad0c-de2ef902ee18",
      "created": 1617624373864,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003005",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6e-7
    },
    {
      "id": "3954819e-960e-4f48-88b9-b705a797ab33",
      "created": 1617610050962,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002942",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 5.9e-7
    },
    {
      "id": "ecdf4b6f-49bc-45a4-ab58-f48e43fdb56e",
      "created": 1617595656752,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00003121",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 6.2e-7
    },
    {
      "id": "bd5170b8-6776-494b-8c3e-23e126ebacf4",
      "created": 1617581113278,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002475",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 5e-7
    },
    {
      "id": "261cb3a9-43ba-4084-ba04-c9efcf371d4c",
      "created": 1617566684934,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002696",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 5.4e-7
    },
    {
      "id": "ddfabe3f-295c-4751-8faf-ac869c89fccc",
      "created": 1617552391829,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002748",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 5.5e-7
    },
    {
      "id": "8568cae8-a0df-43ff-9bf8-f96087d02c9b",
      "created": 1617538100141,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002725",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 5.5e-7
    },
    {
      "id": "dac646e1-600a-4aa9-8b10-4ce24440fd73",
      "created": 1617523559285,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002325",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.7e-7
    },
    {
      "id": "fc4de4ee-9d9f-49db-bb44-fed95d7b0c98",
      "created": 1617509015648,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001849",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.7e-7
    },
    {
      "id": "bb9d8eaf-8325-42de-906c-35209ea3265d",
      "created": 1617494774381,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001936",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "d039ce23-fa0f-405a-9f7b-1c9fbd397851",
      "created": 1617480228788,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002206",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.4e-7
    },
    {
      "id": "ddc05740-45c5-45bc-9636-729615d6c21f",
      "created": 1617466291030,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001946",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "164e7b6d-e25f-4d47-a01a-fc8919d53bf7",
      "created": 1617451644189,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001984",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "6f56bc86-5ab7-4028-8ae4-8cafd6872ada",
      "created": 1617437164646,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001962",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "69bf74ee-1a76-46dc-add7-62f9b3b79670",
      "created": 1617422608331,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001907",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "1bd7d647-12fd-43a3-8000-952e979652d6",
      "created": 1617408267929,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002014",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "08d22821-8ca3-43c8-92e1-8c79b99c91d9",
      "created": 1617393842585,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002363",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.7e-7
    },
    {
      "id": "967083ff-9784-409b-af0d-d89ba3845478",
      "created": 1617379423012,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002245",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.5e-7
    },
    {
      "id": "0d179da1-ca5a-4439-bfa9-d1b2d45e37db",
      "created": 1617365013543,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001801",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.6e-7
    },
    {
      "id": "81549ff4-5931-4648-b579-91969ddd62fc",
      "created": 1617350645436,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001805",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.6e-7
    },
    {
      "id": "c77746ce-a77f-46fa-82e3-93aaa01b4a27",
      "created": 1617336222133,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001911",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.8e-7
    },
    {
      "id": "20ee01fd-9966-4a54-9009-dd72748cdc45",
      "created": 1617321845763,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002001",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "8a0a809a-9421-4b35-b0ee-eee56cff002f",
      "created": 1617307395985,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002204",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.4e-7
    },
    {
      "id": "c3cbc934-b87d-4df0-86fb-ec463d0dbcfa",
      "created": 1617293286286,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002026",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.1e-7
    },
    {
      "id": "cf219540-7686-4823-ab75-d371cf3e6ab8",
      "created": 1617278738661,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001973",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "00ff81c4-b19a-4bef-b3d2-e054e979530f",
      "created": 1617264460436,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001988",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4e-7
    },
    {
      "id": "eaf77d97-51ec-488f-ae16-25ccc17fd7a6",
      "created": 1617250158407,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002128",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.3e-7
    },
    {
      "id": "24a07136-725d-4fa5-b3de-4d5a1875b7fc",
      "created": 1617235424593,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002181",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.4e-7
    },
    {
      "id": "a78354fb-937e-491e-a35b-a6688f8359d7",
      "created": 1617221137421,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002486",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 5e-7
    },
    {
      "id": "ffb33431-f561-4448-9680-73d5c9030e77",
      "created": 1617206751906,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001974",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "e3fadb4f-2dc0-4ef2-9c9c-eb8f76faa111",
      "created": 1617192180887,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001869",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.7e-7
    },
    {
      "id": "b4b8d369-cb05-41cf-8030-a3aefce4091e",
      "created": 1617178258512,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001675",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.4e-7
    },
    {
      "id": "4fb4faef-2dbf-46e7-b4e6-4421849d464a",
      "created": 1617163551832,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001706",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.4e-7
    },
    {
      "id": "3dba7db1-37e1-461b-8f3e-4c3d8db4b2d4",
      "created": 1617149085637,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001672",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.3e-7
    },
    {
      "id": "19db9bec-25d1-4a9f-8fea-d8b6fc957df8",
      "created": 1617134901571,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002042",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.1e-7
    },
    {
      "id": "70c5d0a5-f8b9-421d-9769-fed1efb3a1c8",
      "created": 1617120286258,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001930",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.9e-7
    },
    {
      "id": "7db7f58d-0661-4533-80ce-cada7b5e9594",
      "created": 1617105854075,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001643",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 3.3e-7
    },
    {
      "id": "bde9fd15-f926-4554-b608-8ad32867a9f7",
      "created": 1617091743022,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00002075",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 4.2e-7
    },
    {
      "id": "3e4d9aed-496e-4574-b60a-d4ebb0d99f60",
      "created": 1617062779524,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001365",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 2.7e-7
    },
    {
      "id": "dcc5861e-63e6-4cb3-86b8-7158d9f5573f",
      "created": 1617033854434,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001160",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 2.3e-7
    },
    {
      "id": "dced7b15-fff9-4ee4-8487-8fafa1c827e0",
      "created": 1617005069122,
      "currency": {
        "enumName": "BTC",
        "description": "BTC"
      },
      "amount": "0.00001369",
      "metadata": "{}",
      "accountType": {
        "enumName": "USER",
        "description": "USER"
      },
      "feeAmount": 2.7e-7
    }
  ],
  "pagination": {
    "size": 5000,
    "page": 0,
    "totalPageCount": 1
  }
}


def kk(aa):
    df = pd.DataFrame(aa["list"])
    df.rename(columns={'amount':'gross_amount', 'feeAmount': 'nh_fee', }, inplace=True)
    df["currency"] = df["currency"].astype(str)
    df["currency"] = df["currency"].replace("{'enumName': 'BTC', 'description': 'BTC'}", "BTC", )
    df.drop(columns = ['metadata', 'accountType'], inplace=True)
    df['nh_fee'] = pd.to_numeric(df['nh_fee']).astype(np.float32)
    df['gross_amount'] = pd.to_numeric(df['gross_amount']).astype(np.float32)
    df['net_amount'] = df['gross_amount'] - df['nh_fee']
    df['created_datetime'] = [convert_unix_timestamp_to_pandas_date(i) for i in df['created']]
    df['timestamp'] = df['created_datetime'].dt.round('H')
    df = df.sort_values('timestamp', ascending=True,) # sort by time
    df['net_amount_cumsum'] = df['net_amount'].cumsum() # total bitcoin recieved
    return df


def submit_get_request(headers, endpoint):
  """
  Generic function for GET requests without any parameters. Tries to return JSON, but may return text if that fails.
  @param auth_details: the BASIC AUTH details (username and password tuple)
  @param endpoint: the URL
  @return: the response
  """
  try:
    r = requests.get(endpoint, headers=headers)
  except:
    r = requests.get(endpoint, headers=headers, verify=False)
  try:
    return json.loads(r.text)
  except:
    return r.text


headers = {"Key":api_creds['host'], "Key":api_creds["organisation_id"], "Key":api_creds["key"], "Key":api_creds["secret"]}

headers2 = {"X-Time": str(datetime.datetime.utcnow()),
"X-Nonce": "h5nns8i4w2xuqathpfz4tklwemvk0dup",
"X-Organization-Id": "ef1e775f-5b90-45d8-9e11-e42345885a45",
"X-Auth": "45b3ecd4-b998-41fb-8c28-d911c32a504c:98f27a6cde14aa5ad906509ac8ee7923cd8de253111195eb1d04fa3af0c6bc8b",
"X-Request-Id": "y6q32egnbxhmu1jim1qn0omcor33xxr9",
"X-User-Lang": "en"}
cur_time = datetime.datetime.now()
engine = sqlite3.connect(data_path + "nicehash_data.db")
new_engine = sqlite3.connect(data_path + "nicehash_data_new.db")


def update_payout_data_table():

    a = kk(tt)
    # r = pd.read_sql("select * from payout_data", new_sql_engine).sort_values("timestamp")
    # a = pd.concat([r,p])
    a['timestamp'] = pd.to_datetime(a['timestamp'])
    # a['query_time'] = pd.to_datetime(a['query_time'])
    a['created_datetime'] = pd.to_datetime(a['created_datetime'])
    print(a.head(100).to_string())
    a = a.drop_duplicates(subset=[u for u in a.columns if u != 'query_time'])
    print(a.head(100).to_string())
    a.to_sql(f"payout_data", new_sql_engine, if_exists='replace', index=False)
# logging.info(f"4-hr Data Pull done!")
# payout_data = kk(tt)
# payout_data.to_sql(f"payout_data__{cur_time.strftime('%Y_%m_%d_%H_%M')}", engine, if_exists='replace', index=False)
# payout_data['query_time'] = cur_time
# payout_data[[i for i in payout_data.columns if i != "net_amount_cumsum"]].to_sql(f"payout_data", new_engine, if_exists='append', index=False)