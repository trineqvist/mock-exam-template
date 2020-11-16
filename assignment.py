###### Ignore this
import pytest
import hashlib
_ = 123456789  # just a wrong number, please ignore
###### Stop ignoring

# Some stuff you can/should use ...
# feel free to import additional things from those packages already imported
# or the Python Standard Library (https://docs.python.org/3/library/)
# (if it helps) but do not import other 3rd party packages.

from cobra.io import read_sbml_model
from cobra import Reaction, Metabolite

# Read model (central metabolism model of Escherichia coli)
model = read_sbml_model('e_coli_core.xml')

# General hints:
# 1. Use the E. coli Core model (`model`) in its default configuration if not stated otherwise.
# 2. Remember to undo modifications to the model before continuing with the next task
#    (either make a copy of the model for each task or use the `with model: ...` construct as shown in the exercise).


# 1. Simulate the model. What is the reaction with the largest flux magnitude?
# Hints:
# Solutions/output from cobrapy often provides Pandas data frames or series, so you
# can take full advantage of the included functionality.

# Put your intermediate solution steps here if you have any ...

# Replace _ with you're final calculation step or a variable that contains the final solution.
# reaction_with_largest_flux needs to resolve to a reaction ID from the model (of type str)
reaction_with_largest_flux = _


# 2. What are the exchange reactions in the model that can facilitate the uptake of carbon sources?
# Hints:
# The elemental composition of metabolites is in included in the model.

# Put your intermediate solution steps here if you have any ...

# Replace _ with you're final calculation step or a variable that contains the final solution.
# carbon_source_exchanges needs to a list of reaction IDs from the model (each of type str)
carbon_source_exchanges = _


# 3. What are the carbon sources that E. coli can grow on anaerobically?
# Hints:
# You can use model.slim_optimize(error_value=0.) to return a zero growth rate
# for cases were no feasible solution can be found (which is akin to non-growth)

# Put your intermediate solution steps here if you have any ...

# Replace _ with you're final calculation step or a variable that contains the final solution.
# anaerobic_carbon_sources needs to be a list of reaction IDs from the model (each of type str)

anaerobic_carbon_sources = _


# 4. Add the capability to produce 3-Hydroxypropanoate (3HP) to the full genome-scale model of E. coli (iML1515). What is the maximum production rate of 3HP.

# Hints:
# The GSM iML1515 is included here in the repository (iML1515.xml.gz); `read_sbml_model` can import compressed models (".gz").
# There are two heterologous reaction steps that can be added to facilitate the production of 3HP from malonyl-CoA
# 1. https://www.genome.jp/dbget-bin/www_bget?rn:R00740
# 2. https://www.genome.jp/dbget-bin/www_bget?rn:R09289

# Put your intermediate solution steps here if you have any ...


# Replace _ with you're final calculation step or a variable that contains the final solution.
# max_3hp_production needs to resolve to a number (of type float)

max_3hp_production = _


# 5. What is the maximum production rate of 3HP at 20% growth (also using iML1515)?
# Hints:
# The biomass objective already set in the model should be used to determine the maximum growth rate.

# Put your intermediate solution steps here if you have any ...
    
# Replace _ with you're final calculation step or a variable that contains the final solution.
# production_3hp_20perc_growth needs to resolve to a number (of type float)
production_3hp_20perc_growth = _


#### Tests are happening in the end now ...
###### Don't touch

def test_reaction_with_largest_flux():
    assert type(reaction_with_largest_flux) is str, "reaction_with_largest_flux needs to be a reaction ID of type str."
    assert hashlib.md5(reaction_with_largest_flux.encode('utf-8')).digest() == b'd0c\x0b\x93{J&\x98SQ\x9e\xecC\xdb\x8a'

def test_carbon_source_exchanges():
    assert type(carbon_source_exchanges) is list, "carbon_source_exchanges needs to be a list."
    assert type(carbon_source_exchanges[0]) is str, "carbon_source_exchanges needs to be a list of strings."
    assert set(carbon_source_exchanges) == set(['EX_ac_e', 'EX_acald_e', 'EX_akg_e', 'EX_co2_e', 'EX_etoh_e', 'EX_for_e', 'EX_fru_e',
                                       'EX_fum_e', 'EX_glc__D_e', 'EX_gln__L_e', 'EX_glu__L_e', 'EX_lac__D_e', 'EX_mal__L_e',
                                       'EX_pyr_e', 'EX_succ_e'])

def test_anaerobic_carbon_sources():
    assert type(anaerobic_carbon_sources) is list, "carbon_source_exchanges needs to be a list."
    assert type(anaerobic_carbon_sources[0]) is str, "carbon_source_exchanges needs to be a list of strings."
    assert set(anaerobic_carbon_sources) == set(['EX_fru_e', 'EX_fum_e', 'EX_glc__D_e', 'EX_gln__L_e', 'EX_glu__L_e', 'EX_lac__D_e',
                                             'EX_mal__L_e', 'EX_pyr_e', 'EX_succ_e'])

def test_max_3hp_production():
    assert max_3hp_production == pytest.approx(17.84)

def test_production_3hp_20perc_growth():
    assert production_3hp_20perc_growth == pytest.approx(14.3735)
###### this
