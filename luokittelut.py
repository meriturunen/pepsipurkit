# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:26:15 2020

@author: Meri
"""

import pandas as pd
import requests

req = requests.get('https://valtionavustukset.oph.fi/api/junction-hackathon/dump')
dat = req.json()

#%%
haku = pd.DataFrame(dat['haku'])
loppu = pd.DataFrame(dat['loppuselvitys'])

#%%

osa_alueet  = { 0: '01 Varhaiskasvatus', 1: '02 Esi- ja perusopetus', 2: '03 Toisen asteen koulutus', 3: '04 Ammatillinen koulutus', 4: '05 Vapaa sivistystyö', 
               5: '06 Järjestötoiminta', 6: '07 Muut', 7: '08 Korkeakoulu'}


osa_alueet = [{3: '04 Ammatillinen koulutus'},
                      {0: '01 Varhaiskasvatus'},
                      {5: '06 Järjestötoiminta'},
                      {1: '02 Esi- ja perusopetus'},
                      {1: '02 Esi- ja perusopetus'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {0: '01 Varhaiskasvatus'},
                      {1: '02 Esi- ja perusopetus'},
                      {1: '02 Esi- ja perusopetus'},
                      {1: '02 Esi- ja perusopetus'},
                      {2: '03 Toisen asteen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {4: '05 Vapaa sivistystyö'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {1: '02 Esi- ja perusopetus'},
                      {1: '02 Esi- ja perusopetus'},
                      {1: '02 Esi- ja perusopetus'},
                      {0: '01 Varhaiskasvatus'},
                      {1: '02 Esi- ja perusopetus'},
                      {5: '06 Järjestötoiminta'},
                      {3: '04 Ammatillinen koulutus'},
                      {1: '02 Esi- ja perusopetus'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {0: '01 Varhaiskasvatus'},
                      {2: '03 Toisen asteen koulutus'},
                      {2: '03 Toisen asteen koulutus'},
                      {2: '03 Toisen asteen koulutus'},
                      {1: '02 Esi- ja perusopetus'},
                      {7: '08 Korkeakoulu'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {3: '04 Ammatillinen koulutus'},
                      {1: '02 Esi- ja perusopetus'},
                      {1: '02 Esi- ja perusopetus'},
                      {1: '02 Esi- ja perusopetus'},
                      {2: '03 Toisen asteen koulutus'},
                      {1: '02 Esi- ja perusopetus'},
                      {3: '04 Ammatillinen koulutus'},
                      {2: '03 Toisen asteen koulutus'},
                      {0: '01 Varhaiskasvatus'},
                      {7: '08 Korkeakoulu'},
                      {1: '02 Esi- ja perusopetus'},
                      {1: '02 Esi- ja perusopetus'},
                      {5: '06 Järjestötoiminta'},
                      {1: '02 Esi- ja perusopetus'},
                      {2: '03 Toisen asteen koulutus'},
                      {2: '03 Toisen asteen koulutus'},
                      {5: '06 Järjestötoiminta'},
                      {2: '03 Toisen asteen koulutus'},
                      {7: '08 Korkeakoulu'},
                      {1: '02 Esi- ja perusopetus'},
                      {3: '04 Ammatillinen koulutus'},
                      {2: '03 Toisen asteen koulutus'},
                      {2: '03 Toisen asteen koulutus'},
                      {2: '03 Toisen asteen koulutus'}                      
                      ]
haku['osa_alueet'] = osa_alueet

id_alue_df = haku[['id', 'osa_alueet']]

#%%

morso = id_alue_df['osa_alueet'][0]