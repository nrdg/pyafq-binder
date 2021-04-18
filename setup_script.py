import os.path as op
import AFQ.data as afd
from AFQ.definitions.mask import RoiMask
from AFQ.definitions.mapping import AffMap
from AFQ import api

afd.organize_stanford_data()

myafq = api.AFQ(bids_path=op.join(afd.afq_home, 'stanford_hardi'),
                dmriprep='vistasoft',
                tracking_params={"n_seeds": 1,
                                 "directions": "det",
                                 "odf_model": "DTI",
                                 "seed_mask": RoiMask()},
                bundle_info=["ARC"],
                mapping=AffMap(),
                viz_backend='plotly_no_gif')

myafq.export_all()
