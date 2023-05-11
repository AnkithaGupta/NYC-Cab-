Last login: Mon Apr 10 16:51:36 on ttys004
(base) jemather@monza ~ % pip install fastparquet
Collecting fastparquet
  Downloading fastparquet-2023.2.0-cp39-cp39-macosx_10_9_universal2.whl (792 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 792.6/792.6 kB 11.2 MB/s eta 0:00:00
Collecting pandas>=1.5.0
  Downloading pandas-2.0.0-cp39-cp39-macosx_10_9_x86_64.whl (11.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.8/11.8 MB 29.9 MB/s eta 0:00:00
Requirement already satisfied: packaging in /opt/anaconda3/lib/python3.9/site-packages (from fastparquet) (21.3)
Collecting cramjam>=2.3
  Downloading cramjam-2.6.2-cp39-cp39-macosx_10_9_x86_64.macosx_11_0_arm64.macosx_10_9_universal2.whl (3.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 28.4 MB/s eta 0:00:00
Requirement already satisfied: fsspec in /opt/anaconda3/lib/python3.9/site-packages (from fastparquet) (2022.7.1)
Requirement already satisfied: numpy>=1.20.3 in /opt/anaconda3/lib/python3.9/site-packages (from fastparquet) (1.21.5)
Collecting tzdata>=2022.1
  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 341.8/341.8 kB 10.6 MB/s eta 0:00:00
Requirement already satisfied: pytz>=2020.1 in /opt/anaconda3/lib/python3.9/site-packages (from pandas>=1.5.0->fastparquet) (2023.3)
Collecting python-dateutil>=2.8.2
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 kB 7.9 MB/s eta 0:00:00
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /opt/anaconda3/lib/python3.9/site-packages (from packaging->fastparquet) (3.0.9)
Requirement already satisfied: six>=1.5 in ./.local/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas>=1.5.0->fastparquet) (1.16.0)
Installing collected packages: tzdata, python-dateutil, cramjam, pandas, fastparquet
  Attempting uninstall: python-dateutil
    Found existing installation: python-dateutil 2.8.1
    Uninstalling python-dateutil-2.8.1:
      Successfully uninstalled python-dateutil-2.8.1
  Attempting uninstall: pandas
    Found existing installation: pandas 1.4.4
    Uninstalling pandas-1.4.4:
      Successfully uninstalled pandas-1.4.4
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
conda-repo-cli 1.0.24 requires clyent==1.2.1, but you have clyent 1.2.2 which is incompatible.
conda-repo-cli 1.0.24 requires nbformat==5.4.0, but you have nbformat 5.5.0 which is incompatible.
conda-repo-cli 1.0.24 requires requests==2.28.1, but you have requests 2.28.2 which is incompatible.
Successfully installed cramjam-2.6.2 fastparquet-2023.2.0 pandas-2.0.0 python-dateutil-2.8.2 tzdata-2023.3
(base) jemather@monza ~ % python3
Python 3.9.13 (main, Aug 25 2022, 18:29:29)
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from fastparquet import ParquetFile
pf >>> pf = ParquetFile("/Users/jemather/Downloads/fhv_tripdata_2023-01.parquet")
>>> df = pf.to_pandas()
>>> df
        dispatching_base_num     pickup_datetime    dropOff_datetime  PUlocationID  DOlocationID  SR_Flag Affiliated_base_number
0                     B00008 2023-01-01 00:30:00 2023-01-01 01:00:00           NaN           NaN     <NA>                 B00008
1                     B00078 2023-01-01 00:01:00 2023-01-01 03:15:00           NaN           NaN     <NA>                 B00078
2                     B00111 2023-01-01 00:30:00 2023-01-01 01:05:00           NaN           NaN     <NA>                 B03406
3                     B00112 2023-01-01 00:34:45 2023-01-01 00:52:03           NaN          14.0     <NA>                 B00112
4                     B00112 2023-01-01 00:11:20 2023-01-01 00:22:03           NaN          14.0     <NA>                 B00112
...                      ...                 ...                 ...           ...           ...      ...                    ...
1114315               B03380 2023-01-31 23:32:54 2023-02-01 00:17:17         132.0          66.0     <NA>                 B03380
1114316               B03380 2023-01-31 23:23:14 2023-01-31 23:34:20         229.0         246.0     <NA>                 B03380
1114317               B03380 2023-01-31 23:08:08 2023-01-31 23:20:18         263.0          43.0     <NA>                 B03380
1114318               B03380 2023-01-31 23:43:53 2023-02-01 00:03:14         226.0          24.0     <NA>                 B03404
1114319               B03391 2023-01-31 23:36:50 2023-01-31 23:59:14           NaN          77.0     <NA>                 B03391

[1114320 rows x 7 columns]
>>> df
        dispatching_base_num     pickup_datetime    dropOff_datetime  PUlocationID  DOlocationID  SR_Flag Affiliated_base_number
0                     B00008 2023-01-01 00:30:00 2023-01-01 01:00:00           NaN           NaN     <NA>                 B00008
1                     B00078 2023-01-01 00:01:00 2023-01-01 03:15:00           NaN           NaN     <NA>                 B00078
2                     B00111 2023-01-01 00:30:00 2023-01-01 01:05:00           NaN           NaN     <NA>                 B03406
3                     B00112 2023-01-01 00:34:45 2023-01-01 00:52:03           NaN          14.0     <NA>                 B00112
4                     B00112 2023-01-01 00:11:20 2023-01-01 00:22:03           NaN          14.0     <NA>                 B00112
...                      ...                 ...                 ...           ...           ...      ...                    ...
1114315               B03380 2023-01-31 23:32:54 2023-02-01 00:17:17         132.0          66.0     <NA>                 B03380
1114316               B03380 2023-01-31 23:23:14 2023-01-31 23:34:20         229.0         246.0     <NA>                 B03380
1114317               B03380 2023-01-31 23:08:08 2023-01-31 23:20:18         263.0          43.0     <NA>                 B03380
1114318               B03380 2023-01-31 23:43:53 2023-02-01 00:03:14         226.0          24.0     <NA>                 B03404
1114319               B03391 2023-01-31 23:36:50 2023-01-31 23:59:14           NaN          77.0     <NA>                 B03391

[1114320 rows x 7 columns]
>>> dispatching_base_num.group_by(dispatching_base_num)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dispatching_base_num' is not defined
>>> dispatching_base_num.group_by("dispatching_base_num")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dispatching_base_num' is not defined
>>> dispatching_base_num.groupby("dispatching_base_num")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dispatching_base_num' is not defined
>>> df.groupby("dispatching_base_num")
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fab1001d820>
>>> df.groupby("dispatching_base_num").summary()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/groupby/groupby.py", line 952, in __getattr__
    raise AttributeError(
AttributeError: 'DataFrameGroupBy' object has no attribute 'summary'
>>> df.groupby("dispatching_base_num").summarize()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/groupby/groupby.py", line 952, in __getattr__
    raise AttributeError(
AttributeError: 'DataFrameGroupBy' object has no attribute 'summarize'
>>> df.groupby("dispatching_base_num").count_values()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/groupby/groupby.py", line 952, in __getattr__
    raise AttributeError(
AttributeError: 'DataFrameGroupBy' object has no attribute 'count_values'
>>> df.groupby("dispatching_base_num")
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x7fab000093d0>
>>> df.unique("dispatching_base_num")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/generic.py", line 5989, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'unique'
>>> df.unique("dispatching_base_num")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/generic.py", line 5989, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'unique'
>>> df['dispatching_base_num'].unique()
array(['B00008', 'B00078', 'B00111', 'B00112', 'B00149', 'B00222',
       'B00254', 'B00256', 'B00271', 'B00280', 'B00310', 'B00445',
       'B00446', 'B00459', 'B00647', 'B00692', 'B00706', 'B00756',
       'B00789', 'B00821', 'B00837', 'B00850', 'B00856', 'B00860',
       'B00887', 'B00900', 'B00937', 'B00965', 'B00972', 'B00975',
       'B01061', 'B01065', 'B01079', 'B01083', 'B01087', 'B01145',
       'B01176', 'B01233', 'B01236', 'B01239', 'B01268', 'B01285',
       'B01339', 'B01340', 'B01386', 'B01406', 'B01413', 'B01437',
       'B01452', 'B01454', 'B01455', 'B01466', 'B01509', 'B01536',
       'B01601', 'B01606', 'B01626', 'B01639', 'B01663', 'B01667',
       'B01717', 'B01726', 'B01730', 'B01743', 'B01745', 'B01777',
       'B01843', 'B01899', 'B01958', 'B01963', 'B01984', 'B01995',
       'B02107', 'B02111', 'B02157', 'B02162', 'B02173', 'B02249',
       'B02315', 'B02331', 'B02416', 'B02429', 'B02461', 'B02536',
       'B02537', 'B02546', 'B02550', 'B02677', 'B02719', 'B02728',
       'B02735', 'B02762', 'B02794', 'B02814', 'B02849', 'B02902',
       'B02905', 'B02930', 'B02968', 'B02997', 'B03015', 'B03016',
       'B03033', 'B03041', 'B03046', 'B03060', 'B03171', 'B03174',
       'B03233', 'B03248', 'B03268', 'B03269', 'B03284', 'B03299',
       'B03380', 'B03381', 'B03391', 'B03482', 'B00013', 'B00221',
       'B00225', 'B00277', 'B00350', 'B00381', 'B00412', 'B00608',
       'B00628', 'B01312', 'B01315', 'B01367', 'B01436', 'B01469',
       'B01738', 'B01768', 'B01871', 'B02093', 'B02096', 'B02120',
       'B02148', 'B02285', 'B02437', 'B02557', 'B02655', 'B02661',
       'B02795', 'B02912', 'B03266', 'B03286', 'B03388', 'B00014',
       'B00448', 'B01346', 'B02050', 'B02406', 'B02825', 'B02990',
       'B03309', 'B03320', 'B01616', 'B01803', 'B02699', 'B00429',
       'B00911', 'B01020', 'B02021', 'B02855', 'B03164', 'B00556',
       'B00625', 'B00802', 'B00932', 'B01066', 'B01282', 'B01537',
       'B01800', 'B01877', 'B02352', 'B02391', 'B02641', 'B02770',
       'B03028', 'B03324', 'B01016', 'B01336', 'B01527', 'B01559',
       'B01644', 'B02671', 'B02747', 'B03147', 'B03197', 'B03314',
       'B03338', 'B00009', 'B00037', 'B00823', 'B01280', 'B01534',
       'B01540', 'B02254', 'B02279', 'B02311', 'B02401', 'B02424',
       'B02517', 'B02756', 'B03097', 'B03104', 'B03239', 'B03297',
       'B00054', 'B00095', 'B01081', 'B01124', 'B01259', 'B01311',
       'B01341', 'B01482', 'B01678', 'B01721', 'B01742', 'B01938',
       'B02003', 'B02055', 'B02099', 'B02163', 'B02472', 'B02774',
       'B02799', 'B02909', 'B03051', 'B03055', 'B03100', 'B03157',
       'B03285', 'B00001', 'B01381', 'B01424', 'B01432', 'B01492',
       'B01913', 'B02005', 'B02144', 'B02152', 'B02287', 'B02320',
       'B02462', 'B02509', 'B02627', 'B02670', 'B02934', 'B02998',
       'B01009', 'B01215', 'B01854', 'B01980', 'B02101', 'B02410',
       'B02613', 'B00272', 'B01128', 'B01779', 'B02397', 'B02724',
       'B02811', 'B03349', 'B01364', 'B01593', 'B03206', 'B03367',
       'B00449', 'B01625', 'B01970', 'B02217', 'B02339', 'B02629',
       'B03296', 'B02599', 'B03236', 'B02334', 'B00208', 'B00411',
       'B01470', 'B02298', 'B01183', 'B01273', 'B02738', 'B02897',
       'B02899', 'B03057', 'B03074', 'B01629', 'B02127', 'B03113',
       'B03393', 'B01944', 'B02095', 'B03050', 'B00053', 'B03172',
       'B00597', 'B00889', 'B00948', 'B01710', 'B02782', 'B02784',
       'B02834', 'B02962', 'B03040', 'B03263', 'B03283', 'B00387',
       'B02418', 'B02833', 'B02975', 'B03156', 'B03211', 'B03326',
       'B03333', 'B00623', 'B02531', 'B02594', 'B02737', 'B02760',
       'B02832', 'B02972', 'B03017', 'B03047', 'B03209', 'B03341',
       'B03346', 'B00255', 'B00531', 'B00906', 'B01013', 'B01029',
       'B01417', 'B02573', 'B02731', 'B02846', 'B02868', 'B02881',
       'B03139', 'B03187', 'B03292', 'B03336', 'B03421', 'B00827',
       'B01057', 'B02532', 'B02658', 'B02687', 'B02819', 'B03002',
       'B03116', 'B03276', 'B03281', 'B03335', 'B03455', 'B00652',
       'B02453', 'B02817', 'B03145', 'B03153', 'B03185', 'B03371',
       'B00196', 'B01546', 'B02240', 'B03282', 'B02522', 'B03181',
       'B03262', 'B02664', 'B03107', 'B01306', 'B03081', 'B03030',
       'B02060', 'B03138', 'B03105', 'B03291', 'B02929', 'B02898',
       'B03436', 'B03144', 'B02989', 'B03194', 'B03287', 'B03315',
       'B00559', 'B02901', 'B03061', 'B03199', 'B03329', 'B00151',
       'B02739', 'B03166', 'B03085', 'B03334', 'B02971', 'B03339',
       'B03438', 'B03126', 'B00888', 'B01568', 'B02228', 'B02342',
       'B03064', 'B02301', 'B03258', 'B01928', 'B03417', 'B02924',
       'B02823', 'B03352', 'B03229', 'B02853', 'B03403', 'B01194',
       'B03158', 'B02273', 'B03123', 'B02207', 'B03433', 'B03466',
       'B03018', 'B03038', 'B03256'], dtype=object)
>>> df[df[dispatching_base_num == 'B03404']]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dispatching_base_num' is not defined
>>> df
        dispatching_base_num     pickup_datetime    dropOff_datetime  PUlocationID  DOlocationID  SR_Flag Affiliated_base_number
0                     B00008 2023-01-01 00:30:00 2023-01-01 01:00:00           NaN           NaN     <NA>                 B00008
1                     B00078 2023-01-01 00:01:00 2023-01-01 03:15:00           NaN           NaN     <NA>                 B00078
2                     B00111 2023-01-01 00:30:00 2023-01-01 01:05:00           NaN           NaN     <NA>                 B03406
3                     B00112 2023-01-01 00:34:45 2023-01-01 00:52:03           NaN          14.0     <NA>                 B00112
4                     B00112 2023-01-01 00:11:20 2023-01-01 00:22:03           NaN          14.0     <NA>                 B00112
...                      ...                 ...                 ...           ...           ...      ...                    ...
1114315               B03380 2023-01-31 23:32:54 2023-02-01 00:17:17         132.0          66.0     <NA>                 B03380
1114316               B03380 2023-01-31 23:23:14 2023-01-31 23:34:20         229.0         246.0     <NA>                 B03380
1114317               B03380 2023-01-31 23:08:08 2023-01-31 23:20:18         263.0          43.0     <NA>                 B03380
1114318               B03380 2023-01-31 23:43:53 2023-02-01 00:03:14         226.0          24.0     <NA>                 B03404
1114319               B03391 2023-01-31 23:36:50 2023-01-31 23:59:14           NaN          77.0     <NA>                 B03391

[1114320 rows x 7 columns]
>>> df[df["dispatching_base_num" == 'B03404']]
Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3652, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 147, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 176, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: False

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/frame.py", line 3760, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3654, in get_loc
    raise KeyError(key) from err
KeyError: False
>>> df["dispatching_base_num"]
0          B00008
1          B00078
2          B00111
3          B00112
4          B00112
            ...
1114315    B03380
1114316    B03380
1114317    B03380
1114318    B03380
1114319    B03391
Name: dispatching_base_num, Length: 1114320, dtype: object
>>> df[df["dispatching_base_num" == 'B03404']]
Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3652, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 147, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 176, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: False

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/frame.py", line 3760, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3654, in get_loc
    raise KeyError(key) from err
KeyError: False
>>> df[df["dispatching_base_num" == 'B03391']]
Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3652, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 147, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 176, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7080, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7088, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: False

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/frame.py", line 3760, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 3654, in get_loc
    raise KeyError(key) from err
KeyError: False
>>> pf = ParquetFile("/Users/jemather/Downloads/fhvhv_tripdata_2022-11.parquet")
>>> df = pf.to_pandas()
>>> df.head()
  hvfhs_license_num dispatching_base_num originating_base_num    request_datetime   on_scene_datetime  ... shared_request_flag shared_match_flag  access_a_ride_flag  wav_request_flag  wav_match_flag
0            HV0003               B03404               B03404 2022-11-01 00:04:09 2022-11-01 00:10:11  ...                   N                 N                                     N               N
1            HV0003               B03404               B03404 2022-11-01 00:42:26 2022-11-01 00:45:33  ...                   N                 N                                     N               N
2            HV0003               B03404               B03404 2022-11-01 00:11:53 2022-11-01 00:17:15  ...                   N                 N                                     N               N
3            HV0003               B03404               B03404 2022-11-01 00:45:30 2022-11-01 00:49:39  ...                   N                 N                                     N               N
4            HV0005               B03406                 None 2022-10-31 23:56:33                 NaT  ...                   N                 N                   N                 N               N

[5 rows x 24 columns]
>>> pf
<Parquet File: {'name': '/Users/jemather/Downloads/fhvhv_tripdata_2022-11.parquet', 'columns': ['hvfhs_license_num', 'dispatching_base_num', 'originating_base_num', 'request_datetime', 'on_scene_datetime', 'pickup_datetime', 'dropoff_datetime', 'PULocationID', 'DOLocationID', 'trip_miles', 'trip_time', 'base_passenger_fare', 'tolls', 'bcf', 'sales_tax', 'congestion_surcharge', 'airport_fee', 'tips', 'driver_pay', 'shared_request_flag', 'shared_match_flag', 'access_a_ride_flag', 'wav_request_flag', 'wav_match_flag'], 'partitions': [], 'rows': 18085896, 'row_groups': 1}>
>>> df
         hvfhs_license_num dispatching_base_num originating_base_num    request_datetime   on_scene_datetime  ... shared_request_flag shared_match_flag  access_a_ride_flag  wav_request_flag  wav_match_flag
0                   HV0003               B03404               B03404 2022-11-01 00:04:09 2022-11-01 00:10:11  ...                   N                 N                                     N               N
1                   HV0003               B03404               B03404 2022-11-01 00:42:26 2022-11-01 00:45:33  ...                   N                 N                                     N               N
2                   HV0003               B03404               B03404 2022-11-01 00:11:53 2022-11-01 00:17:15  ...                   N                 N                                     N               N
3                   HV0003               B03404               B03404 2022-11-01 00:45:30 2022-11-01 00:49:39  ...                   N                 N                                     N               N
4                   HV0005               B03406                 None 2022-10-31 23:56:33                 NaT  ...                   N                 N                   N                 N               N
...                    ...                  ...                  ...                 ...                 ...  ...                 ...               ...                 ...               ...             ...
18085891            HV0003               B03404               B03404 2022-11-30 22:55:04 2022-11-30 23:01:07  ...                   N                 N                                     N               N
18085892            HV0003               B03404               B03404 2022-11-30 23:21:07 2022-11-30 23:23:35  ...                   N                 N                                     N               N
18085893            HV0003               B03404               B03404 2022-11-30 23:48:51 2022-11-30 23:52:14  ...                   N                 N                                     N               N
18085894            HV0003               B03404               B03404 2022-11-30 23:16:39 2022-11-30 23:20:46  ...                   N                 N                                     N               N
18085895            HV0003               B03404               B03404 2022-11-30 23:40:29 2022-11-30 23:43:58  ...                   N                 N                                     N               N

[18085896 rows x 24 columns]
>>> df['hvfhs_license_num'].unique()
array(['HV0003', 'HV0005'], dtype=object)
>>> df.columns
Index(['hvfhs_license_num', 'dispatching_base_num', 'originating_base_num',
       'request_datetime', 'on_scene_datetime', 'pickup_datetime',
       'dropoff_datetime', 'PULocationID', 'DOLocationID', 'trip_miles',
       'trip_time', 'base_passenger_fare', 'tolls', 'bcf', 'sales_tax',
       'congestion_surcharge', 'airport_fee', 'tips', 'driver_pay',
       'shared_request_flag', 'shared_match_flag', 'access_a_ride_flag',
       'wav_request_flag', 'wav_match_flag'],
      dtype='object')
>>> df['PULocationID']
0            61
1           209
2           181
3           107
4            41
           ...
18085891    255
18085892    146
18085893    134
18085894    220
18085895    242
Name: PULocationID, Length: 18085896, dtype: int64
>>> df['DOLocationID']
0            61
1            79
2           170
3            80
4           241
           ...
18085891    146
18085892    134
18085893     28
18085894    250
18085895    185
Name: DOLocationID, Length: 18085896, dtype: int64
>>> hv = df
>>> hv = df.copy(deep=True)
>>> taxi = ParquetFile("/Users/jemather/Downloads/yellow_tripdata_2022-11.parquet").to_pandas()
>>> taxi
         VendorID tpep_pickup_datetime tpep_dropoff_datetime  passenger_count  trip_distance  RatecodeID  ... tip_amount  tolls_amount  improvement_surcharge  total_amount  congestion_surcharge  airport_fee
0               1  2022-11-01 00:51:22   2022-11-01 00:56:24              1.0            0.6         1.0  ...       0.00           0.0                    0.3          5.80                   0.0          0.0
1               1  2022-11-01 00:39:43   2022-11-01 00:48:44              0.0            1.8         1.0  ...       3.05           0.0                    0.3         15.35                   2.5          0.0
2               1  2022-11-01 00:55:01   2022-11-01 01:01:35              0.0            2.0         1.0  ...       2.36           0.0                    0.3         14.16                   2.5          0.0
3               1  2022-11-01 00:24:49   2022-11-01 00:31:04              2.0            1.0         1.0  ...       0.00           0.0                    0.3          9.80                   2.5          0.0
4               1  2022-11-01 00:37:32   2022-11-01 00:42:23              2.0            0.8         1.0  ...       0.00           0.0                    0.3          9.30                   2.5          0.0
...           ...                  ...                   ...              ...            ...         ...  ...        ...           ...                    ...           ...                   ...          ...
3252712         1  2022-11-30 23:17:09   2022-11-30 23:27:15              NaN            0.0         NaN  ...       0.00           0.0                    0.3         16.76                   NaN          NaN
3252713         2  2022-11-30 23:48:48   2022-12-01 00:05:48              NaN            4.1         NaN  ...       2.00           0.0                    0.3         18.89                   NaN          NaN
3252714         1  2022-11-30 23:04:36   2022-11-30 23:13:39              NaN            1.4         NaN  ...       1.18           0.0                    0.3         12.98                   NaN          NaN
3252715         1  2022-11-30 23:18:37   2022-11-30 23:30:48              NaN            2.5         NaN  ...       2.15           0.0                    0.3         16.45                   NaN          NaN
3252716         1  2022-11-30 23:30:50   2022-11-30 23:51:14              NaN            0.0         NaN  ...       0.00           0.0                    0.3         28.27                   NaN          NaN

[3252717 rows x 19 columns]
>>> taxi.columns
Index(['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
       'passenger_count', 'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
       'PULocationID', 'DOLocationID', 'payment_type', 'fare_amount', 'extra',
       'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
       'total_amount', 'congestion_surcharge', 'airport_fee'],
      dtype='object')
>>> taxi['PULocationID']
0          151
1           90
2          137
3          158
4          249
          ...
3252712    144
3252713     45
3252714    163
3252715    161
3252716     74
Name: PULocationID, Length: 3252717, dtype: int64
>>> pf
<Parquet File: {'name': '/Users/jemather/Downloads/fhvhv_tripdata_2022-11.parquet', 'columns': ['hvfhs_license_num', 'dispatching_base_num', 'originating_base_num', 'request_datetime', 'on_scene_datetime', 'pickup_datetime', 'dropoff_datetime', 'PULocationID', 'DOLocationID', 'trip_miles', 'trip_time', 'base_passenger_fare', 'tolls', 'bcf', 'sales_tax', 'congestion_surcharge', 'airport_fee', 'tips', 'driver_pay', 'shared_request_flag', 'shared_match_flag', 'access_a_ride_flag', 'wav_request_flag', 'wav_match_flag'], 'partitions': [], 'rows': 18085896, 'row_groups': 1}>
>>> df
         hvfhs_license_num dispatching_base_num originating_base_num    request_datetime   on_scene_datetime  ... shared_request_flag shared_match_flag  access_a_ride_flag  wav_request_flag  wav_match_flag
0                   HV0003               B03404               B03404 2022-11-01 00:04:09 2022-11-01 00:10:11  ...                   N                 N                                     N               N
1                   HV0003               B03404               B03404 2022-11-01 00:42:26 2022-11-01 00:45:33  ...                   N                 N                                     N               N
2                   HV0003               B03404               B03404 2022-11-01 00:11:53 2022-11-01 00:17:15  ...                   N                 N                                     N               N
3                   HV0003               B03404               B03404 2022-11-01 00:45:30 2022-11-01 00:49:39  ...                   N                 N                                     N               N
4                   HV0005               B03406                 None 2022-10-31 23:56:33                 NaT  ...                   N                 N                   N                 N               N
...                    ...                  ...                  ...                 ...                 ...  ...                 ...               ...                 ...               ...             ...
18085891            HV0003               B03404               B03404 2022-11-30 22:55:04 2022-11-30 23:01:07  ...                   N                 N                                     N               N
18085892            HV0003               B03404               B03404 2022-11-30 23:21:07 2022-11-30 23:23:35  ...                   N                 N                                     N               N
18085893            HV0003               B03404               B03404 2022-11-30 23:48:51 2022-11-30 23:52:14  ...                   N                 N                                     N               N
18085894            HV0003               B03404               B03404 2022-11-30 23:16:39 2022-11-30 23:20:46  ...                   N                 N                                     N               N
18085895            HV0003               B03404               B03404 2022-11-30 23:40:29 2022-11-30 23:43:58  ...                   N                 N                                     N               N

[18085896 rows x 24 columns]
>>> df.columns
Index(['hvfhs_license_num', 'dispatching_base_num', 'originating_base_num',
       'request_datetime', 'on_scene_datetime', 'pickup_datetime',
       'dropoff_datetime', 'PULocationID', 'DOLocationID', 'trip_miles',
       'trip_time', 'base_passenger_fare', 'tolls', 'bcf', 'sales_tax',
       'congestion_surcharge', 'airport_fee', 'tips', 'driver_pay',
       'shared_request_flag', 'shared_match_flag', 'access_a_ride_flag',
       'wav_request_flag', 'wav_match_flag'],
      dtype='object')
>>> hv.columns
Index(['hvfhs_license_num', 'dispatching_base_num', 'originating_base_num',
       'request_datetime', 'on_scene_datetime', 'pickup_datetime',
       'dropoff_datetime', 'PULocationID', 'DOLocationID', 'trip_miles',
       'trip_time', 'base_passenger_fare', 'tolls', 'bcf', 'sales_tax',
       'congestion_surcharge', 'airport_fee', 'tips', 'driver_pay',
       'shared_request_flag', 'shared_match_flag', 'access_a_ride_flag',
       'wav_request_flag', 'wav_match_flag'],
      dtype='object')
>>> taxi.columns
Index(['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
       'passenger_count', 'trip_distance', 'RatecodeID', 'store_and_fwd_flag',
       'PULocationID', 'DOLocationID', 'payment_type', 'fare_amount', 'extra',
       'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge',
       'total_amount', 'congestion_surcharge', 'airport_fee'],
      dtype='object')
>>> main_data = hv[['pickup_datetime','dropoff_datetime','PULocationID','DOLocationId', 'trip_miles', 'base_passenger_fare', 'shared_request_flag', 'shared_match_flag']]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/frame.py", line 3766, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5876, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5938, in _raise_if_missing
    raise KeyError(f"{not_found} not in index")
KeyError: "['DOLocationId'] not in index"
>>> main_data = hv[['pickup_datetime','dropoff_datetime','PULocationID','DOLocationID', 'trip_miles', 'base_passenger_fare', 'shared_request_flag', 'shared_match_flag']]
>>> taxi_data = taxi[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'PULocationID', 'DOLocationID', 'trip_distance', 'fare_amount']]
>>> taxi_data['shared_request_flag'] = None
<stdin>:1: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
>>> taxi_data = taxi[['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'PULocationID', 'DOLocationID', 'trip_distance', 'fare_amount']].copy(deep=True)
>>> taxi_data['shared_request_flag'] = None
>>> taxi_data['shared_match_flag'] = None
>>> main_data = main_data.copy(deep=True)
>>> main_data['highvolume'] = 1
>>> taxi_data['highvolume'] = 0
>>> out = main_data.append(taxi_data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/generic.py", line 5989, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'append'
>>> out = main_data.concat(taxi_data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/generic.py", line 5989, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'concat'
>>> out = pd.concat(main_data, taxi_data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pd' is not defined
>>> out = pandas.concat(main_data, taxi_data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pandas' is not defined
>>> import pandas as pd
>>> out = pd.concat(main_data, taxi_data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: concat() takes 1 positional argument but 2 were given
>>> out = pd.concat([main_data, taxi_data])
>>> out
            pickup_datetime    dropoff_datetime  PULocationID  DOLocationID  trip_miles  base_passenger_fare  ... shared_match_flag highvolume  tpep_pickup_datetime tpep_dropoff_datetime trip_distance  fare_amount
0       2022-11-01 00:10:31 2022-11-01 00:17:28            61            61       1.040                 7.91  ...                 N          1                   NaT                   NaT           NaN          NaN
1       2022-11-01 00:46:33 2022-11-01 00:58:18           209            79       2.070                14.48  ...                 N          1                   NaT                   NaT           NaN          NaN
2       2022-11-01 00:19:16 2022-11-01 00:46:19           181           170       8.270                27.37  ...                 N          1                   NaT                   NaT           NaN          NaN
3       2022-11-01 00:50:18 2022-11-01 01:08:10           107            80       5.020                26.74  ...                 N          1                   NaT                   NaT           NaN          NaN
4       2022-11-01 00:01:41 2022-11-01 00:20:33            41           241       6.322                22.34  ...                 N          1                   NaT                   NaT           NaN          NaN
...                     ...                 ...           ...           ...         ...                  ...  ...               ...        ...                   ...                   ...           ...          ...
3252712                 NaT                 NaT           144           249         NaN                  NaN  ...              None          0   2022-11-30 23:17:09   2022-11-30 23:27:15           0.0        13.46
3252713                 NaT                 NaT            45           106         NaN                  NaN  ...              None          0   2022-11-30 23:48:48   2022-12-01 00:05:48           4.1        13.59
3252714                 NaT                 NaT           163           141         NaN                  NaN  ...              None          0   2022-11-30 23:04:36   2022-11-30 23:13:39           1.4         8.00
3252715                 NaT                 NaT           161           143         NaN                  NaN  ...              None          0   2022-11-30 23:18:37   2022-11-30 23:30:48           2.5        10.50
3252716                 NaT                 NaT            74           232         NaN                  NaN  ...              None          0   2022-11-30 23:30:50   2022-11-30 23:51:14           0.0        24.97

[21338613 rows x 13 columns]
>>> taxi_data.columns = main_data.columns
>>> out = pd.concat([main_data, taxi_data])
>>> out
            pickup_datetime    dropoff_datetime  PULocationID  DOLocationID  trip_miles  base_passenger_fare shared_request_flag shared_match_flag  highvolume
0       2022-11-01 00:10:31 2022-11-01 00:17:28            61            61       1.040                 7.91                   N                 N           1
1       2022-11-01 00:46:33 2022-11-01 00:58:18           209            79       2.070                14.48                   N                 N           1
2       2022-11-01 00:19:16 2022-11-01 00:46:19           181           170       8.270                27.37                   N                 N           1
3       2022-11-01 00:50:18 2022-11-01 01:08:10           107            80       5.020                26.74                   N                 N           1
4       2022-11-01 00:01:41 2022-11-01 00:20:33            41           241       6.322                22.34                   N                 N           1
...                     ...                 ...           ...           ...         ...                  ...                 ...               ...         ...
3252712 2022-11-30 23:17:09 2022-11-30 23:27:15           144           249       0.000                13.46                None              None           0
3252713 2022-11-30 23:48:48 2022-12-01 00:05:48            45           106       4.100                13.59                None              None           0
3252714 2022-11-30 23:04:36 2022-11-30 23:13:39           163           141       1.400                 8.00                None              None           0
3252715 2022-11-30 23:18:37 2022-11-30 23:30:48           161           143       2.500                10.50                None              None           0
3252716 2022-11-30 23:30:50 2022-11-30 23:51:14            74           232       0.000                24.97                None              None           0

[21338613 rows x 9 columns]
>>> out.to_csv("/Users/jemather/Dropbox/monza/taxi.csv")
>>> out.group_by("PULocationID").agg({'highvolume': "sum", 'highvolume': "count"})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/generic.py", line 5989, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'group_by'
>>> out.groupby("PULocationID").agg({'highvolume': "sum", 'highvolume': "count"})
              highvolume
PULocationID
1                    882
2                     47
3                  36341
4                  63262
5                   4819
...                  ...
261                87504
262               118630
263               172895
264                46971
265                 7573

[263 rows x 1 columns]
>>> out.groupby("PULocationID").agg({'highvolume': "sum", 'h': "count"})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/groupby/generic.py", line 1271, in aggregate
    result = op.agg()
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 163, in agg
    return self.agg_dict_like()
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 403, in agg_dict_like
    arg = self.normalize_dictlike_arg("agg", selected_obj, arg)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 535, in normalize_dictlike_arg
    raise KeyError(f"Column(s) {cols_sorted} do not exist")
KeyError: "Column(s) ['h'] do not exist"
>>> out.groupby("PULocationID").agg({'highvolume': "sum", 'pickup_datetie': "count"})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/groupby/generic.py", line 1271, in aggregate
    result = op.agg()
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 163, in agg
    return self.agg_dict_like()
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 403, in agg_dict_like
    arg = self.normalize_dictlike_arg("agg", selected_obj, arg)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 535, in normalize_dictlike_arg
    raise KeyError(f"Column(s) {cols_sorted} do not exist")
KeyError: "Column(s) ['pickup_datetie'] do not exist"
>>> out.groupby("PULocationID").agg({'highvolume': "sum", 'pickup_datetine': "count"})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/groupby/generic.py", line 1271, in aggregate
    result = op.agg()
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 163, in agg
    return self.agg_dict_like()
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 403, in agg_dict_like
    arg = self.normalize_dictlike_arg("agg", selected_obj, arg)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/apply.py", line 535, in normalize_dictlike_arg
    raise KeyError(f"Column(s) {cols_sorted} do not exist")
KeyError: "Column(s) ['pickup_datetine'] do not exist"
>>> out.groupby("PULocationID").agg({'highvolume': "sum", 'pickup_datetime': "count"})
              highvolume  pickup_datetime
PULocationID
1                      3              882
2                     45               47
3                  36292            36341
4                  59549            63262
5                   4776             4819
...                  ...              ...
261                71538            87504
262                74664           118630
263               104240           172895
264                    0            46971
265                  893             7573

[263 rows x 2 columns]
>>> temp =out.groupby("PULocationID").agg({'highvolume': "sum", 'pickup_datetime': "count"})
>>> temp['pct'] = temp]
  File "<stdin>", line 1
    temp['pct'] = temp]
                      ^
SyntaxError: unmatched ']'
>>> temp['pct'] = temp['highvolume']/temp['pickup_datetime']
>>> temp
              highvolume  pickup_datetime       pct
PULocationID
1                      3              882  0.003401
2                     45               47  0.957447
3                  36292            36341  0.998652
4                  59549            63262  0.941308
5                   4776             4819  0.991077
...                  ...              ...       ...
261                71538            87504  0.817540
262                74664           118630  0.629385
263               104240           172895  0.602909
264                    0            46971  0.000000
265                  893             7573  0.117919

[263 rows x 3 columns]
>>> temp.to_csv("/Users/jemather/Dropbox/monza/results.csv"
... )
>>> zones = pd.read_csv("/Users/jemather/Downloads/taxi+_zone_lookup.csv")
>>> zones
     LocationID        Borough                     Zone service_zone
0             1            EWR           Newark Airport          EWR
1             2         Queens              Jamaica Bay    Boro Zone
2             3          Bronx  Allerton/Pelham Gardens    Boro Zone
3             4      Manhattan            Alphabet City  Yellow Zone
4             5  Staten Island            Arden Heights    Boro Zone
..          ...            ...                      ...          ...
260         261      Manhattan       World Trade Center  Yellow Zone
261         262      Manhattan           Yorkville East  Yellow Zone
262         263      Manhattan           Yorkville West  Yellow Zone
263         264        Unknown                       NV          NaN
264         265        Unknown                      NaN          NaN

[265 rows x 4 columns]
>>> temp.merge(zones, left_on = "PU
KeyboardInterrupt
>>> temp = temp.reset_index()
>>> temp
     PULocationID  highvolume  pickup_datetime       pct
0               1           3              882  0.003401
1               2          45               47  0.957447
2               3       36292            36341  0.998652
3               4       59549            63262  0.941308
4               5        4776             4819  0.991077
..            ...         ...              ...       ...
258           261       71538            87504  0.817540
259           262       74664           118630  0.629385
260           263      104240           172895  0.602909
261           264           0            46971  0.000000
262           265         893             7573  0.117919

[263 rows x 4 columns]
>>> temp.merge(zones, left_on = 'PULocationID', right_on = 'LocationID')
     PULocationID  highvolume  pickup_datetime       pct  LocationID        Borough                     Zone service_zone
0               1           3              882  0.003401           1            EWR           Newark Airport          EWR
1               2          45               47  0.957447           2         Queens              Jamaica Bay    Boro Zone
2               3       36292            36341  0.998652           3          Bronx  Allerton/Pelham Gardens    Boro Zone
3               4       59549            63262  0.941308           4      Manhattan            Alphabet City  Yellow Zone
4               5        4776             4819  0.991077           5  Staten Island            Arden Heights    Boro Zone
..            ...         ...              ...       ...         ...            ...                      ...          ...
258           261       71538            87504  0.817540         261      Manhattan       World Trade Center  Yellow Zone
259           262       74664           118630  0.629385         262      Manhattan           Yorkville East  Yellow Zone
260           263      104240           172895  0.602909         263      Manhattan           Yorkville West  Yellow Zone
261           264           0            46971  0.000000         264        Unknown                       NV          NaN
262           265         893             7573  0.117919         265        Unknown                      NaN          NaN

[263 rows x 8 columns]
>>> temp.merge(zones, left_on = 'PULocationID', right_on = 'LocationID').to_csv("/Users/jemather/Dropbox/monza/results.csv")
>>> temp =out.groupby(["PULocationID", "DOLocationID"]).agg({'highvolume': "sum", 'pickup_datetime': "count"})
>>> temp
                           highvolume  pickup_datetime
PULocationID DOLocationID
1            1                      2              761
             68                     0                1
             100                    0                1
             113                    0                1
             132                    0                3
...                               ...              ...
265          261                    0               10
             262                    0               14
             263                    0               41
             264                    0              119
             265                  294             2067

[59757 rows x 2 columns]
>>> temp = temp.reset_index()
>>> temp = temp.merge(zones, left_on = 'PULocationID', right_on = 'LocationID').to_csv("/Users/jemather/Dropbox/monza/results.csv")
>>> temp
>>> temp =out.groupby(["PULocationID", "DOLocationID"]).agg({'highvolume': "sum", 'pickup_datetime': "count"})
>>> temp
                           highvolume  pickup_datetime
PULocationID DOLocationID
1            1                      2              761
             68                     0                1
             100                    0                1
             113                    0                1
             132                    0                3
...                               ...              ...
265          261                    0               10
             262                    0               14
             263                    0               41
             264                    0              119
             265                  294             2067

[59757 rows x 2 columns]
>>> out temp.merge(zones, left_on = 'PULocationID', right_on = 'LocationID')
  File "<stdin>", line 1
    out temp.merge(zones, left_on = 'PULocationID', right_on = 'LocationID')
        ^
SyntaxError: invalid syntax
>>> out = temp.merge(zones, left_on = 'PULocationID', right_on = 'LocationID')
>>> out
       highvolume  pickup_datetime  LocationID  Borough            Zone service_zone
0               2              761           1      EWR  Newark Airport          EWR
1               0                1           1      EWR  Newark Airport          EWR
2               0                1           1      EWR  Newark Airport          EWR
3               0                1           1      EWR  Newark Airport          EWR
4               0                3           1      EWR  Newark Airport          EWR
...           ...              ...         ...      ...             ...          ...
59752           0               10         265  Unknown             NaN          NaN
59753           0               14         265  Unknown             NaN          NaN
59754           0               41         265  Unknown             NaN          NaN
59755           0              119         265  Unknown             NaN          NaN
59756         294             2067         265  Unknown             NaN          NaN

[59757 rows x 6 columns]
>>> temp
                           highvolume  pickup_datetime
PULocationID DOLocationID
1            1                      2              761
             68                     0                1
             100                    0                1
             113                    0                1
             132                    0                3
...                               ...              ...
265          261                    0               10
             262                    0               14
             263                    0               41
             264                    0              119
             265                  294             2067

[59757 rows x 2 columns]
>>> out.columns = ['fhv_rides', 'all_rides', 'PULocationID', b
...
KeyboardInterrupt
>>> temp.reset_index()
       PULocationID  DOLocationID  highvolume  pickup_datetime
0                 1             1           2              761
1                 1            68           0                1
2                 1           100           0                1
3                 1           113           0                1
4                 1           132           0                3
...             ...           ...         ...              ...
59752           265           261           0               10
59753           265           262           0               14
59754           265           263           0               41
59755           265           264           0              119
59756           265           265         294             2067

[59757 rows x 4 columns]
>>> temp = temp.reset_index()
>>> temp
       PULocationID  DOLocationID  highvolume  pickup_datetime
0                 1             1           2              761
1                 1            68           0                1
2                 1           100           0                1
3                 1           113           0                1
4                 1           132           0                3
...             ...           ...         ...              ...
59752           265           261           0               10
59753           265           262           0               14
59754           265           263           0               41
59755           265           264           0              119
59756           265           265         294             2067

[59757 rows x 4 columns]
>>> temp.merge(zones, left_on = 'PULocationID', right_on = 'LocationID')
       PULocationID  DOLocationID  highvolume  pickup_datetime  LocationID  Borough            Zone service_zone
0                 1             1           2              761           1      EWR  Newark Airport          EWR
1                 1            68           0                1           1      EWR  Newark Airport          EWR
2                 1           100           0                1           1      EWR  Newark Airport          EWR
3                 1           113           0                1           1      EWR  Newark Airport          EWR
4                 1           132           0                3           1      EWR  Newark Airport          EWR
...             ...           ...         ...              ...         ...      ...             ...          ...
59752           265           261           0               10         265  Unknown             NaN          NaN
59753           265           262           0               14         265  Unknown             NaN          NaN
59754           265           263           0               41         265  Unknown             NaN          NaN
59755           265           264           0              119         265  Unknown             NaN          NaN
59756           265           265         294             2067         265  Unknown             NaN          NaN

[59757 rows x 8 columns]
>>> temp = temp.merge(zones, left_on = 'PULocationID', right_on = 'LocationID')
>>> temp
       PULocationID  DOLocationID  highvolume  pickup_datetime  LocationID  Borough            Zone service_zone
0                 1             1           2              761           1      EWR  Newark Airport          EWR
1                 1            68           0                1           1      EWR  Newark Airport          EWR
2                 1           100           0                1           1      EWR  Newark Airport          EWR
3                 1           113           0                1           1      EWR  Newark Airport          EWR
4                 1           132           0                3           1      EWR  Newark Airport          EWR
...             ...           ...         ...              ...         ...      ...             ...          ...
59752           265           261           0               10         265  Unknown             NaN          NaN
59753           265           262           0               14         265  Unknown             NaN          NaN
59754           265           263           0               41         265  Unknown             NaN          NaN
59755           265           264           0              119         265  Unknown             NaN          NaN
59756           265           265         294             2067         265  Unknown             NaN          NaN

[59757 rows x 8 columns]
>>> temp.columns
Index(['PULocationID', 'DOLocationID', 'highvolume', 'pickup_datetime',
       'LocationID', 'Borough', 'Zone', 'service_zone'],
      dtype='object')
>>> temp.columns = ['PULocationID', 'DOLocationID', 'fhv_rides', 'all_rides', 'PULocationID_drop', 'PUBorough', 'PUZone', 'PU]service_zone'
... ]
>>> temp.columns = ['PULocationID', 'DOLocationID', 'fhv_rides', 'all_rides', 'PULocationID_drop', 'PUBorough', 'PUZone', 'PU]service_zone']
>>> temp
       PULocationID  DOLocationID  fhv_rides  all_rides  PULocationID_drop PUBorough          PUZone PU]service_zone
0                 1             1          2        761                  1       EWR  Newark Airport             EWR
1                 1            68          0          1                  1       EWR  Newark Airport             EWR
2                 1           100          0          1                  1       EWR  Newark Airport             EWR
3                 1           113          0          1                  1       EWR  Newark Airport             EWR
4                 1           132          0          3                  1       EWR  Newark Airport             EWR
...             ...           ...        ...        ...                ...       ...             ...             ...
59752           265           261          0         10                265   Unknown             NaN             NaN
59753           265           262          0         14                265   Unknown             NaN             NaN
59754           265           263          0         41                265   Unknown             NaN             NaN
59755           265           264          0        119                265   Unknown             NaN             NaN
59756           265           265        294       2067                265   Unknown             NaN             NaN

[59757 rows x 8 columns]
>>> temp.merge(zones, left_on = 'DOLocationID', right_on = 'LocationID')
       PULocationID  DOLocationID  fhv_rides  all_rides  PULocationID_drop      PUBorough                       PUZone PU]service_zone  LocationID        Borough              Zone service_zone
0                 1             1          2        761                  1            EWR               Newark Airport             EWR           1            EWR    Newark Airport          EWR
1                 3             1         18         18                  3          Bronx      Allerton/Pelham Gardens       Boro Zone           1            EWR    Newark Airport          EWR
2                 4             1        555        579                  4      Manhattan                Alphabet City     Yellow Zone           1            EWR    Newark Airport          EWR
3                 5             1        147        147                  5  Staten Island                Arden Heights       Boro Zone           1            EWR    Newark Airport          EWR
4                 6             1        119        119                  6  Staten Island      Arrochar/Fort Wadsworth       Boro Zone           1            EWR    Newark Airport          EWR
...             ...           ...        ...        ...                ...            ...                          ...             ...         ...            ...               ...          ...
59752           110           110          5          5                110  Staten Island             Great Kills Park       Boro Zone         110  Staten Island  Great Kills Park    Boro Zone
59753           118           110          3          3                118  Staten Island  Heartland Village/Todt Hill       Boro Zone         110  Staten Island  Great Kills Park    Boro Zone
59754           176           110          5          5                176  Staten Island                      Oakwood       Boro Zone         110  Staten Island  Great Kills Park    Boro Zone
59755           210           110          1          1                210       Brooklyn               Sheepshead Bay       Boro Zone         110  Staten Island  Great Kills Park    Boro Zone
59756           228           110          1          1                228       Brooklyn             Sunset Park West       Boro Zone         110  Staten Island  Great Kills Park    Boro Zone

[59757 rows x 12 columns]
>>> temp = temp.merge(zones, left_on = 'DOLocationID', right_on = 'LocationID')
>>> cols = temp.columns[:9]
>>> cols
Index(['PULocationID', 'DOLocationID', 'fhv_rides', 'all_rides',
       'PULocationID_drop', 'PUBorough', 'PUZone', 'PU]service_zone',
       'LocationID'],
      dtype='object')
>>> cols = temp.columns[:8]
>>> temp.columns = [''PULocationID_drop', 'PUBorough', 'PUZone', 'PU]service_zone',çPULocationID', 'DOLocationID', 'fhv_rides', 'all_rides',
KeyboardInterrupt
>>> temp.columns = ['PULocationID', 'DOLocationID', 'fhv_rides', 'all_rides','PULocationID_drop', 'PUBorough', 'PUZone', 'PU]service_zone']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/generic.py", line 6002, in __setattr__
    return object.__setattr__(self, name, value)
  File "pandas/_libs/properties.pyx", line 69, in pandas._libs.properties.AxisProperty.__set__
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/generic.py", line 730, in _set_axis
    self._mgr.set_axis(axis, labels)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/internals/managers.py", line 225, in set_axis
    self._validate_set_axis(axis, new_labels)
  File "/opt/anaconda3/lib/python3.9/site-packages/pandas/core/internals/base.py", line 70, in _validate_set_axis
    raise ValueError(
ValueError: Length mismatch: Expected axis has 12 elements, new values have 8 elements
>>> temp.columns = ['PULocationID', 'DOLocationID', 'fhv_rides', 'all_rides','PULocationID_drop', 'PUBorough', 'PUZone', 'PU]service_zone', 'DOLocationID_drop', 'DOBorough', 'DOZone', 'DOservice_zone']
>>> temp.columns = ['PULocationID', 'DOLocationID', 'fhv_rides', 'all_rides','PULocationID_drop', 'PUBorough', 'PUZone', 'PUservice_zone', 'DOLocationID_drop', 'DOBorough', 'DOZone', 'DOservice_zone']
>>> temp
       PULocationID  DOLocationID  fhv_rides  all_rides  PULocationID_drop      PUBorough                       PUZone PUservice_zone  DOLocationID_drop      DOBorough            DOZone DOservice_zone
0                 1             1          2        761                  1            EWR               Newark Airport            EWR                  1            EWR    Newark Airport            EWR
1                 3             1         18         18                  3          Bronx      Allerton/Pelham Gardens      Boro Zone                  1            EWR    Newark Airport            EWR
2                 4             1        555        579                  4      Manhattan                Alphabet City    Yellow Zone                  1            EWR    Newark Airport            EWR
3                 5             1        147        147                  5  Staten Island                Arden Heights      Boro Zone                  1            EWR    Newark Airport            EWR
4                 6             1        119        119                  6  Staten Island      Arrochar/Fort Wadsworth      Boro Zone                  1            EWR    Newark Airport            EWR
...             ...           ...        ...        ...                ...            ...                          ...            ...                ...            ...               ...            ...
59752           110           110          5          5                110  Staten Island             Great Kills Park      Boro Zone                110  Staten Island  Great Kills Park      Boro Zone
59753           118           110          3          3                118  Staten Island  Heartland Village/Todt Hill      Boro Zone                110  Staten Island  Great Kills Park      Boro Zone
59754           176           110          5          5                176  Staten Island                      Oakwood      Boro Zone                110  Staten Island  Great Kills Park      Boro Zone
59755           210           110          1          1                210       Brooklyn               Sheepshead Bay      Boro Zone                110  Staten Island  Great Kills Park      Boro Zone
59756           228           110          1          1                228       Brooklyn             Sunset Park West      Boro Zone                110  Staten Island  Great Kills Park      Boro Zone

[59757 rows x 12 columns]
>>> temp.to_csv("/Users/jemather/Dropbox/monza/results.csv"
... )
>>> out
       highvolume  pickup_datetime  LocationID  Borough            Zone service_zone
0               2              761           1      EWR  Newark Airport          EWR
1               0                1           1      EWR  Newark Airport          EWR
2               0                1           1      EWR  Newark Airport          EWR
3               0                1           1      EWR  Newark Airport          EWR
4               0                3           1      EWR  Newark Airport          EWR
...           ...              ...         ...      ...             ...          ...
59752           0               10         265  Unknown             NaN          NaN
59753           0               14         265  Unknown             NaN          NaN
59754           0               41         265  Unknown             NaN          NaN
59755           0              119         265  Unknown             NaN          NaN
59756         294             2067         265  Unknown             NaN          NaN

[59757 rows x 6 columns]
>>> out = pd.concat([main_data, taxi_data])
>>> out.groupby(["PULocationID", ).agg({'highvolume': "sum", 'pickup_datetime': "count"})
KeyboardInterrupt
>>> out['hour'] =
KeyboardInterrupt
>>> out
            pickup_datetime    dropoff_datetime  PULocationID  DOLocationID  trip_miles  base_passenger_fare shared_request_flag shared_match_flag  highvolume
0       2022-11-01 00:10:31 2022-11-01 00:17:28            61            61       1.040                 7.91                   N                 N           1
1       2022-11-01 00:46:33 2022-11-01 00:58:18           209            79       2.070                14.48                   N                 N           1
2       2022-11-01 00:19:16 2022-11-01 00:46:19           181           170       8.270                27.37                   N                 N           1
3       2022-11-01 00:50:18 2022-11-01 01:08:10           107            80       5.020                26.74                   N                 N           1
4       2022-11-01 00:01:41 2022-11-01 00:20:33            41           241       6.322                22.34                   N                 N           1
...                     ...                 ...           ...           ...         ...                  ...                 ...               ...         ...
3252712 2022-11-30 23:17:09 2022-11-30 23:27:15           144           249       0.000                13.46                None              None           0
3252713 2022-11-30 23:48:48 2022-12-01 00:05:48            45           106       4.100                13.59                None              None           0
3252714 2022-11-30 23:04:36 2022-11-30 23:13:39           163           141       1.400                 8.00                None              None           0
3252715 2022-11-30 23:18:37 2022-11-30 23:30:48           161           143       2.500                10.50                None              None           0
3252716 2022-11-30 23:30:50 2022-11-30 23:51:14            74           232       0.000                24.97                None              None           0

[21338613 rows x 9 columns]
>>> out['hour'] = pd.DateTime(pickup_datetime).hour()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'pandas' has no attribute 'DateTime'
>>> out['hour'] = pd.DateTime(pickup_datetime).hour()
KeyboardInterrupt
>>> out['hour'] = pd.DateTime(pickup_datetime).hour
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'pandas' has no attribute 'DateTime'
>>> out['hour'] = pd.DateTime(pickup_datetime).dt.hour
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'pandas' has no attribute 'DateTime'
>>> out['hour'] = out['pickup_datetime'].dt.hour
>>> out
            pickup_datetime    dropoff_datetime  PULocationID  DOLocationID  trip_miles  base_passenger_fare shared_request_flag shared_match_flag  highvolume  hour
0       2022-11-01 00:10:31 2022-11-01 00:17:28            61            61       1.040                 7.91                   N                 N           1     0
1       2022-11-01 00:46:33 2022-11-01 00:58:18           209            79       2.070                14.48                   N                 N           1     0
2       2022-11-01 00:19:16 2022-11-01 00:46:19           181           170       8.270                27.37                   N                 N           1     0
3       2022-11-01 00:50:18 2022-11-01 01:08:10           107            80       5.020                26.74                   N                 N           1     0
4       2022-11-01 00:01:41 2022-11-01 00:20:33            41           241       6.322                22.34                   N                 N           1     0
...                     ...                 ...           ...           ...         ...                  ...                 ...               ...         ...   ...
3252712 2022-11-30 23:17:09 2022-11-30 23:27:15           144           249       0.000                13.46                None              None           0    23
3252713 2022-11-30 23:48:48 2022-12-01 00:05:48            45           106       4.100                13.59                None              None           0    23
3252714 2022-11-30 23:04:36 2022-11-30 23:13:39           163           141       1.400                 8.00                None              None           0    23
3252715 2022-11-30 23:18:37 2022-11-30 23:30:48           161           143       2.500                10.50                None              None           0    23
3252716 2022-11-30 23:30:50 2022-11-30 23:51:14            74           232       0.000                24.97                None              None           0    23

[21338613 rows x 10 columns]
>>> out.groupby(["PULocationID", 'hour']).agg({'highvolume': "sum", 'pickup_datetime': "count"})
                   highvolume  pickup_datetime
PULocationID hour
1            0              0                3
             1              0                1
             2              0                4
             3              0               13
             4              0               21
...                       ...              ...
265          19            32              262
             20            24              207
             21            38              224
             22            41              260
             23            28              208

[6255 rows x 2 columns]
>>> out.groupby(["PULocationID", 'hour']).agg({'highvolume': "sum", 'pickup_datetime': "count"}).reset_index()
      PULocationID  hour  highvolume  pickup_datetime
0                1     0           0                3
1                1     1           0                1
2                1     2           0                4
3                1     3           0               13
4                1     4           0               21
...            ...   ...         ...              ...
6250           265    19          32              262
6251           265    20          24              207
6252           265    21          38              224
6253           265    22          41              260
6254           265    23          28              208

[6255 rows x 4 columns]
>>> byhour = out.groupby(["PULocationID", 'hour']).agg({'highvolume': "sum", 'pickup_datetime': "count"}).reset_index()
>>> byhour
      PULocationID  hour  highvolume  pickup_datetime
0                1     0           0                3
1                1     1           0                1
2                1     2           0                4
3                1     3           0               13
4                1     4           0               21
...            ...   ...         ...              ...
6250           265    19          32              262
6251           265    20          24              207
6252           265    21          38              224
6253           265    22          41              260
6254           265    23          28              208

[6255 rows x 4 columns]
>>> byhour.columns = ['PULocationID', 'hour', 'hv', 'total']
>>> byhour['pct'] = byhour['hv']/byhour['total']
>>> byhour.merge(zones, left_on = "PULocationID", right_on = "LocationID")
      PULocationID  hour  hv  total       pct  LocationID  Borough            Zone service_zone
0                1     0   0      3  0.000000           1      EWR  Newark Airport          EWR
1                1     1   0      1  0.000000           1      EWR  Newark Airport          EWR
2                1     2   0      4  0.000000           1      EWR  Newark Airport          EWR
3                1     3   0     13  0.000000           1      EWR  Newark Airport          EWR
4                1     4   0     21  0.000000           1      EWR  Newark Airport          EWR
...            ...   ...  ..    ...       ...         ...      ...             ...          ...
6250           265    19  32    262  0.122137         265  Unknown             NaN          NaN
6251           265    20  24    207  0.115942         265  Unknown             NaN          NaN
6252           265    21  38    224  0.169643         265  Unknown             NaN          NaN
6253           265    22  41    260  0.157692         265  Unknown             NaN          NaN
6254           265    23  28    208  0.134615         265  Unknown             NaN          NaN

[6255 rows x 9 columns]
>>> byhour.merge(zones, left_on = "PULocationID", right_on = "LocationID").to_csv("/Users/jemather/Dropbox/monza/byhour.csv", index=False)
>>>
