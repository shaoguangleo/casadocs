#
# stub function definition file for docstring parsing
#

def virtualconcat(vis, concatvis='', freqtol='', dirtol='', respectname=True, visweightscale=[''], keepcopy=False, copypointing=True):
    r"""
Concatenate several visibility data sets into a multi-MS

Parameters
   - **vis** (stringArray) - List of names of input visibility files to be concatenated
   - **concatvis** (string='') - Name of the output visibility file (a multi-MS)
   - **freqtol** (variant='') - Frequency shift tolerance for considering data as the same spwid
   - **dirtol** (variant='') - Direction shift tolerance for considering data as the same field
   - **respectname** (bool=True) - If true, fields with a different name are not merged even if their direction agrees
   - **visweightscale** (doubleArray=['']) - List of the weight scaling factors to be applied to the individual MSs
   - **keepcopy** (bool=False) - If true, a copy of the input MSs is kept in their original place.
   - **copypointing** (bool=True) - If true, keep the POINTING table information in the output MMS. If false, don\'t.


Description
   .. note:: **NOTE**: This task behaves mostly like the task **concat**,
      except that the result is an MMS and that the original MSs
      become part of the concatenated MS (unless you set
      *keepcopy=True*).

   The list of data sets given in the *vis* argument are moved into
   an outputMulti-MS data set and virtually concatenated. This task
   will modify the input datasets by moving and reindexing them.If
   you want to keep a copy of your original data, please set the
   parameter *keepcopy* to True. It only makes sense to use
   **virtualconcat** with *'keepcopy=True'*, instead of **concat**,
   if you need to create an MMS instead of an MS.

   There is no limit to the number of input data sets. If none of the
   input data sets have any scratch columns (MODEL and CORRECTED
   columns), none are created in the *concatvis* dataset. Otherwise
   these columns arecreated on output and initialized to their
   default value (1 in MODEL column,data in CORRECTED column) for
   those data with no input columns.

   Spectral windows for each data set with the same channelization,
   and within aspecified frequency tolerance of another data set,
   will be combined into onespectral window. A field position in one
   data set that is within a specified direction toleranceof another
   field position in any other data set will be combined into
   onefield. The field names need not be the same (only their
   position is used). Each appended dataset is assigned a new
   observation ID if the correspondingrows in the observation table
   are not the same.

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *vis*
      

   Name of input visibility files to be combined. No default

   .. rubric:: *concatvis*
      

   Name of visibility file that will contain the concatenated data.

   .. note:: **NOTE**: If this file exits on disk then the input files are
      added to this file. Otherwise the new file contains the
      concatenated data. Be careful here when concatenating to an
      existing file.

   No default.

   .. rubric:: *freqtol*
      

   Frequency shift tolerance for considering data to be in the same
   spw ID. The number of channels must also be the same. Default: '',
   i.e., do not combine unless frequencies are equal. Example:
   *freqtol='10MHz'* will not combine spw ID unless they are within
   10 MHz.

   .. note:: **NOTE**: This option is useful to combine spectral windows
      with very slight frequency differences caused by Doppler
      tracking, for example.

   .. rubric:: *dirtol*
      

   Direction shift tolerance for considering data as the same field.
   Default: '' means always combine. Example: *dirtol='1.arcsec'*
   will not combine data for a field unless their phase center differ
   by less than 1 arcsec. If the field names are different in the
   input data sets, the name in the output data set will be the first
   relevant data set in the list.

   .. rubric:: *respectname*
      

   If True, fields with a different name are not merged even if their
   direction agrees (within *dirtol*). Default: True

   .. rubric:: *visweightscale*
      

   The weights of the individual MSs will be scaled in the
   concatenated output MS by the factors in this list. Useful for
   handling heterogeneous arrays. Use **plotms** to inspect the "Wt"
   column as a reference for determining the scaling factors. See the
   CASA Docs Chapter Pages on `Data
   Weights <https://casa.nrao.edu/casadocs-devel/stable/calibration-and-visibility-data/data-weights>`__
   for more details. Example: *visweightscale=[1.,3.,3.]*, which
   scales the weights of the second and third MS by a factor 3.
   Default: [] (empty list) or no scaling

   .. rubric:: *keepcopy*
      

   If True, a copy of the input MSs is kept in their original place.
   Default: False

   .. rubric:: *copypointing*
      

   If True, the POINTING table information will be present in the
   output. If False, the result is an empty POINTING table. Default:
   True

    """
    pass
