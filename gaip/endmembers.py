#! /usr/bin/env python

from __future__ import absolute_import, print_function
import numpy

"""
End members used in fractional cover. Josh Sixsmith is the person to talk to about this code... though you shouldn't really
need to know about it as it is only used internally by groundcover_componentsL5_reflect_v3.
"""





def sum_weight(date, help=False):
    '''
    Retrieves the sum to one weighting constraint used for deriving the
    fractional components of a Landsat (5TM/7ETM+) image.

    :param date:
        A string of the form yyyy_mm_dd used to request the required
        sum to one weighting constraint. The weights are derived at the same
        time the synthetic spectral endmembers are derived.

    :param help:
        A boolean to dictate whether or not to display the available dates.
        Default is False.

    Example:

        >>> sumToOneWeight = sum_weight(date='2013_01_08')
        >>> sum_weight(help=True)

    :return:
        A floating point value representing the sum to one weighting
        constraint.

    Notes:

        The weighting constraint differs by date/version.

        * 2009_08_10 returns 0.01
        * 2012_12_07 returns 0.02
        * 2013_01_08 returns 0.02
        * 2014_07_23 returns 1.0

    Contacts:

        * Peter Scarth; peter.scarth@qld.gov.au
        * Josh Sixsmith; joshua.sixsmith@ga.gov.au
    '''
    #2013_01_08
    #2012_12_07
    #2009_08_10
    if help:
        print('Available dates for the sum to one weighting constraints  are:')
        print('2009_08_10')
        print('2012_12_07')
        print('2013_01_08')
        print('2014_07_23')

        return


    instr = str(date)

    return {
        '2013_01_08' : 0.02,
        '2012_12_07' : 0.02,
        '2009_08_10' : 0.01,
        '2014_07_23' : 1.0,
           }.get(instr, 'Error')


def endmember_version(date='', help=False):
    '''
    Retrieves the synthetic spectral endmembers used for deriving the
    fractional components of a Landsat (5TM/7ETM+) image.

    :param date:
        A string of the form yyyy_mm_dd used to request the required
        synthetic spectral endmembers. The date indicates when the endmembers
        were created (or as close as possible) by Peter Scarth.

    :param help:
        A boolean to dictate whether or not to display the available dates.
        Default is False.

    Example:

        >>> end_member = endmember_version(date='2013_01_08')
        >>> endmember_version(help=True)

    :return:
        A numpy array containing the synthetic spectral endmembers.

    Notes:

        The shape of the array differs by the date/version requested.

        * 2009_08_10 returns (56, 4)
        * 2012_12_07 returns (56, 4)
        * 2013_01_08 returns (59, 4)
        * 2014_07_23 returns (60, 4)

        Also, the different dates/versions return different fractional
        components.

        * 2009_08_10 gives green, dead, bare1 and bare2
        * 2012_12_07 gives green, dead, bare1 and bare2
        * 2013_01_08 gives green, dead1, dead2 and bare
        * 2014_07_23 gives green, dead, bare1 and bare2

    Contact:

        * Peter Scarth; peter.scarth@qld.gov.au
        * Josh Sixsmith; joshua.sixsmith@ga.gov.au
    '''

    #def sum_weight(date):
    #    #2013_01_08
    #    #2012_12_07
    #    #2009_08_10

    #    instr = str(date)

    #    return {
    #        '2013_01_08' : 0.02,
    #        '2012_12_07' : 0.02,
    #        '2009_08_10' : 0.01,
    #           }.get(instr, 'Error')

    def get_endmembers(date, sumToOneWeight):

        instr = str(date)

        return {
            '2013_01_08' : numpy.array([[2.777620655803357888e-02,2.761958246706466488e-02,2.980504927638840534e-02,3.002317495935927227e-02],\
  [-3.217380728650560268e-02,-3.198771680263017003e-02,-3.288275204084301073e-02,-3.205269993210731888e-02],\
  [6.796882946822377196e-03,4.079285257396094225e-03,4.777066418641001157e-03,5.577807494019349464e-03],\
  [1.328371707660326237e-02,1.264616515246487320e-02,1.195900510785656914e-02,1.096689099582264307e-02],\
  [-1.761485082086775705e-02,-1.546445130711776236e-02,-1.725477302178379108e-02,-1.803212951596809901e-02],\
  [-5.424018167719665481e-03,-3.186794286120691114e-03,-4.272131857520704810e-03,-4.149382660524386125e-03],\
  [-4.321711922905287565e-03,-1.140419149442576524e-02,-1.000277414343896110e-02,-8.140969749060984750e-03],\
  [2.356114256558785106e-02,2.403410997816551875e-02,2.460396690859500968e-02,2.734314841627123044e-02],\
  [2.294193221788897938e-03,6.863965474659524009e-03,6.807311681588914566e-03,2.823505387316067698e-03],\
  [-6.912354518466031286e-03,-5.543662758195273474e-03,-5.645236191240123221e-03,-5.724178387486781282e-03],\
  [-1.261144359340614016e-02,-1.285143295055899554e-02,-1.293309128419801828e-02,-1.348384991565387825e-02],\
  [-4.133430607521327519e-04,9.272004480433014475e-04,-5.698792391385177139e-05,9.034588815693027960e-04],\
  [1.485694984218449526e-02,1.413580124210375710e-02,1.537053005370155739e-02,1.506616907944931076e-02],\
  [1.400701924042715291e-02,1.321910417917565583e-02,1.373120702380079862e-02,1.273657316053342786e-02],\
  [1.353907993476456684e-02,1.769072890848010990e-02,1.704965556156661302e-02,1.580396906215581973e-02],\
  [-3.199322392469316351e-02,-3.136318783055952464e-02,-3.272080711120763791e-02,-3.518684180006623891e-02],\
  [-9.504231661449313862e-03,-1.321027960095731528e-02,-1.234882699721474159e-02,-8.662108554591738813e-03],\
  [1.002958212366582280e-02,9.003247208585217487e-03,8.666948438112151432e-03,7.518054536810164605e-03],\
  [1.209428589543305732e-02,1.330420647400529233e-02,1.219280565559660925e-02,1.083096230187280233e-02],\
  [1.202239672019374955e-02,1.409609783137818519e-02,1.430657717050396946e-02,1.343643370139184674e-02],\
  [-1.123409784745246776e-02,-1.290429378193452478e-02,-1.353350984654671033e-02,-1.298754058932468335e-02],\
  [7.158544083043502822e-03,1.025248607045884872e-02,9.045289318324612957e-03,8.813064647353482245e-03],\
  [-1.371379813894114431e-02,-1.842557023411172529e-02,-1.411554395134652189e-02,-1.370727473746159372e-02],\
  [1.076459422945670596e-02,1.273934794005364066e-02,1.202702817001729228e-02,1.233302797659361488e-02],\
  [-3.875993380974203026e-03,1.424997278836270592e-03,1.866188099857479452e-03,1.881832027188377800e-03],\
  [7.873417306544594572e-04,1.617115346951038778e-03,1.388690308151508800e-03,6.430535543345451558e-04],\
  [1.439003305161308359e-02,1.434948011241226132e-02,1.531571480181474591e-02,1.548619806039957386e-02],\
  [-6.897523221877789601e-03,-4.512245552215881327e-03,-8.186218923591833535e-03,-7.346011001159360315e-03],\
  [-4.418249116910418807e-03,-6.865047851593538732e-03,-6.412011089839565921e-03,-5.110788297065601941e-03],\
  [-1.405638466029517954e-02,-1.665375936702572640e-02,-1.640962837469809796e-02,-1.604290892504047633e-02],\
  [-1.487399383282169037e-02,-1.715425925570597879e-02,-1.722456836996929391e-02,-1.536849736374391352e-02],\
  [1.013525095009635071e-02,1.218931789492763186e-02,1.176100613461788548e-02,1.011280617035977686e-02],\
  [3.371583289361147285e-04,-1.327929211447257101e-03,7.034832311793831183e-04,3.764480252997269246e-04],\
  [7.817885450462552788e-03,9.520459711981014289e-03,7.994259479881554720e-03,7.659890614314317225e-03],\
  [-4.632116069606707041e-03,-8.189113739281850615e-03,-6.816468708780820500e-03,-6.169255982079187295e-03],\
  [4.498862972587684716e-04,8.356505585705544577e-04,6.943322532742283917e-04,5.904849516895087271e-04],\
  [-1.135863395463956047e-03,-1.048045851769919190e-03,-1.134955808895339157e-03,-1.080831356168136196e-03],\
  [-2.191741938317171880e-03,-2.455973124107526523e-03,-2.428231599578084109e-03,-2.432333792135544723e-03],\
  [1.702319426862321846e-03,1.762538455024271426e-03,1.793715409879262455e-03,1.799034567844016953e-03],\
  [1.496447901603269398e-03,1.101478022463535291e-03,1.849816714536399020e-03,1.831465133683246116e-03],\
  [-3.354195465612455304e-04,-3.176240279274801731e-04,-6.469017549489881631e-04,-5.705232895770457995e-04],\
  [-9.996390568657767105e-04,-1.147955604540262667e-03,-1.229031826954048645e-03,-1.209839350152063907e-03],\
  [2.079719380655255419e-03,2.635067252473373423e-03,2.300277523902831585e-03,2.231031503660944621e-03],\
  [-1.962161210945455141e-03,-2.139178666661481053e-03,-2.191611887916780025e-03,-2.203797322870529752e-03],\
  [5.616304677207857414e-04,4.961192343607978561e-04,6.759719324420015779e-04,7.004796434464368110e-04],\
  [-1.543746915347098472e-02,-1.622655175591887836e-02,-1.659151592980423126e-02,-1.625662620013852699e-02],\
  [-1.012334817100682058e-02,-1.136470747892550856e-02,-1.146408828657622184e-02,-1.053977495547379906e-02],\
  [2.416442343839092597e-03,-4.157851299162059443e-04,2.959645413800449966e-03,3.582915009778713748e-03],\
  [1.642316580279169075e-02,1.881966308028112933e-02,1.691510155300215631e-02,1.637971513686470662e-02],\
  [5.533865064676259798e-03,4.772827044946651755e-03,4.738687225353317711e-03,4.307470992476612054e-03],\
  [-1.899059134595227141e-03,-7.393762595159438129e-04,-1.366785465514660592e-03,-1.592860506491564163e-03],\
  [1.951428677771314610e-03,3.264386865744239516e-03,2.821711878933591024e-03,2.440152510550727682e-03],\
  [1.086887367700179689e-03,5.302704975014560507e-04,3.359022965358689390e-03,3.361772128153661145e-03],\
  [-3.659450947671698783e-03,-4.206333513759127722e-03,-6.475420466083007219e-03,-6.053703079525999189e-03],\
  [-1.018241144033982032e-03,-2.285151861705874646e-03,-1.962799636912524338e-03,-1.851652899029707089e-03],\
  [-3.064286713319604605e-03,-1.157715128209892488e-03,-4.948201904717060978e-03,-5.181822061861071811e-03],\
  [1.877159314925155604e-03,1.648168689328203011e-03,1.992140835925275497e-03,1.876100816831601176e-03],\
  [3.783131742348041886e-03,5.218300703927385500e-03,6.756974095972631544e-03,6.592468366169286498e-03],\
  [sumToOneWeight, sumToOneWeight, sumToOneWeight, sumToOneWeight]]),
            '2012_12_07' : numpy.array(
    [[5.843314445767331528e-03,4.982015683924682740e-03,5.539976665781481437e-03,8.907699516039251086e-03],\
    [-5.520336090814032329e-03,-3.632099688857756171e-03,-3.122719546799471516e-03,-4.821034002830539705e-03],\
    [-4.474994057501213360e-03,-5.588682996328735858e-03,-5.512333898677437491e-03,-7.321329611799454531e-03],\
    [6.716102243679532551e-04,1.490821389780739832e-04,-1.580203968479465971e-03,-3.139806054864524576e-03],\
    [-8.945238117660148439e-03,-7.474046718819113422e-03,-7.877903258002222353e-03,-7.635470931884697117e-03],\
    [-1.583299275543261983e-02,-1.418896900848586225e-02,-1.340692624729080372e-02,-1.217881301896714050e-02],\
    [1.069967242802368455e-02,6.284219087945549023e-03,6.662673643450979163e-03,5.024400897433702919e-03],\
    [1.334949467139988008e-02,1.190383366477570579e-02,1.509260463238526126e-02,1.513273770423946563e-02],\
    [1.109736515503443287e-02,1.345489045207996608e-02,1.022974107311813534e-02,1.089972112326014451e-02],\
    [-4.198374295063293619e-03,-3.257898454915673665e-03,-2.879941982813860688e-03,-1.928415437051176013e-03],\
    [-7.375681368299397307e-03,-7.770556398037790739e-03,-8.530801638277388591e-03,-9.488496627846799633e-03],\
    [-1.977309170517606665e-04,-5.108769807197998097e-04,6.230232517712246381e-04,3.394862833146878537e-04],\
    [1.632825471229902570e-02,1.579232795393669883e-02,1.536886417750834601e-02,1.518761584018183189e-02],\
    [3.571465357945596570e-03,4.320104715684475183e-03,2.611796764408784097e-03,-3.716414569906317800e-05],\
    [-6.227316591356035422e-03,-3.818581939867433158e-03,-3.737976927036762952e-03,-2.090622102390838309e-03],\
    [-9.616215124166251071e-03,-9.101215109031942502e-03,-1.168135847930288837e-02,-1.110307364331969589e-02],\
    [-1.038211140520670615e-02,-1.207187691076975003e-02,-8.750314785439585255e-03,-9.017180516669271242e-03],\
    [-1.406732188694884318e-03,-2.294606275351834899e-03,-3.598218728987842997e-03,-4.557891672252704571e-03],\
    [7.004601118744329530e-03,5.998841940451494006e-03,4.897143120195129526e-03,4.653757361336374569e-03],\
    [-2.452033512054039958e-03,-8.068875679010296433e-04,-1.162737675061478780e-03,-4.235045387016023177e-05],\
    [3.463805504208520777e-03,1.832955052377547873e-03,1.750147284185571634e-03,3.728425008046197444e-04],\
    [8.421381220442263754e-03,7.014038788726111549e-03,6.975106534369546023e-03,6.500130068922005920e-03],\
    [-5.564413653486299620e-03,-4.851963922615817014e-03,-5.086883963161413849e-03,-5.053526947455514243e-03],\
    [-6.363183227858183397e-04,-1.609040971336781248e-04,5.803889390904981137e-04,1.538136658731530972e-03],\
    [2.133675794273826032e-02,2.264917384809743764e-02,2.363713191872900132e-02,2.469916568037380106e-02],\
    [-3.668393460845143124e-03,-2.579713700404942349e-03,-3.061602743338001902e-03,-2.015791986333638312e-03],\
    [2.648107765020987336e-03,2.855592908564151544e-03,2.952077141683168669e-03,2.563345173064296260e-03],\
    [6.253825763080510421e-03,5.149478539373390437e-03,6.078397155080058310e-03,5.678639087699359142e-03],\
    [-5.727342927189800481e-03,-5.407552426956162631e-03,-4.062090486775472332e-03,-2.440461376900634940e-03],\
    [-4.396889597315486314e-03,-4.686499083391225569e-03,-4.912379000076912139e-03,-5.290644929065989668e-03],\
    [-1.367917924572093803e-02,-1.452442710925251970e-02,-1.309899951237997184e-02,-1.362352068024666983e-02],\
    [1.356407847554825553e-02,1.431559210227458662e-02,1.295445894807488972e-02,1.336870251141550510e-02],\
    [-2.252383009663462467e-03,-1.637499294563223365e-03,-2.140199334134519713e-03,-2.023482230085962060e-03],\
    [4.645446076168768465e-03,3.949119275425724829e-03,3.720448104528099615e-03,3.086973540834452544e-03],\
    [-1.216010377081579684e-02,-1.249553637700784835e-02,-1.203879158556966922e-02,-1.145864029274976104e-02],\
    [6.576810578015146805e-05,1.487835686492277644e-04,1.105934821638792200e-04,1.129629113562405352e-04],\
    [-6.244753721888751923e-05,-1.069744276987839507e-04,-4.025731978172188597e-05,-1.058192258115923500e-04],\
    [-6.286752839286402364e-04,-6.936372848089661109e-04,-7.751205576482191788e-04,-8.744931159590370274e-04],\
    [9.777619446019233246e-04,9.498405882270643608e-04,9.749552743457013271e-04,9.826143830101502150e-04],\
    [-8.861679067118325022e-05,-5.777676316404136176e-06,-3.211532544189139892e-05,8.353620707397115084e-05],\
    [4.552300995903088088e-04,4.765769119979866098e-04,5.493490842782924356e-04,5.403137961017921839e-04],\
    [-8.398462042911639504e-04,-8.878344751694745114e-04,-9.012773090988187219e-04,-9.133894333146040526e-04],\
    [2.390832257774019431e-04,2.990480810680585708e-04,2.825815015790461029e-04,4.016341632207630742e-04],\
    [-9.669225725448632415e-06,-1.202835134699676894e-04,-1.994482349777118135e-04,-3.906918597033950924e-04],\
    [-1.737088376760541298e-04,-1.254803806716222334e-04,-6.656242849515571643e-05,3.754364091842595972e-05],\
    [1.350569079306896542e-02,1.125767731503250768e-02,1.192082423422114769e-02,1.239449921969503106e-02],\
    [-1.493033846139976608e-03,-2.892432582455235421e-03,-1.753387944483844564e-03,-1.591877294903211448e-03],\
    [-1.198996668923842275e-02,-8.733418712905709896e-03,-8.254761373725688633e-03,-6.043473246488783104e-03],\
    [-4.333100035358513637e-04,2.924040083206375421e-04,-1.664680780758972481e-04,-4.940216489879736914e-04],\
    [-6.421542732689770536e-03,-6.036332340385188941e-03,-6.859357995032233646e-03,-7.538171866247031332e-03],\
    [2.676501890445672025e-03,2.479869528047138998e-03,2.384861674160212303e-03,1.891119773554709354e-03],\
    [-2.660533617772328600e-03,-2.013148185258595117e-03,-2.092357960983574818e-03,-1.782200062262824514e-03],\
    [5.696438408407671246e-04,4.315392978990682500e-04,1.799839750615037754e-04,-1.630903885789752698e-06],\
    [-1.352392215382145066e-03,-1.139195682929482027e-03,-7.758615820837736279e-04,-2.823657804124836846e-04],\
    [-1.920058902348865428e-04,-7.137420214734345328e-04,-7.616042181362052063e-04,-1.028101193806582993e-03],\
    [sumToOneWeight, sumToOneWeight, sumToOneWeight, sumToOneWeight]]),
            '2009_08_10' : numpy.array(
    [[2.311656148208681566e-02,2.363106348429514642e-02,2.405194231262888088e-02,1.732115965976090133e-02],\
      [-7.655932690993010048e-02,-7.783372022130559398e-02,-7.948145117014031313e-02,-7.571955863846036028e-02],\
      [5.092569335241311362e-02,5.227084180313924799e-02,5.422335743858286428e-02,5.060125912381038121e-02],\
      [4.432805864904891362e-03,4.479543062231678037e-03,2.894900399359918563e-03,6.434448811872802224e-04],\
      [-2.866540918560802828e-02,-2.789253691182672079e-02,-2.811924006485310573e-02,-2.516885485822679958e-02],\
      [9.400035338432501109e-02,9.588233072826733705e-02,9.702461606330489707e-02,1.013899871336205044e-01],\
      [-1.051209439740863338e-02,-1.073142524246834158e-02,-8.858061578513549972e-03,-1.366820845114208316e-02],\
      [-9.491453497411110954e-03,-1.204789364403721294e-02,-1.158207893624211074e-02,-1.180098416782078552e-02],\
      [-3.955649627031056735e-03,-1.216789099235550137e-03,-1.722670381748648031e-03,-4.475534865036078121e-03],\
      [-1.048025368855387898e-02,-1.173869689689119485e-02,-1.398054963416196263e-02,-1.319284909916433254e-02],\
      [4.637121326585704612e-02,4.831646748809415026e-02,5.011030474033312254e-02,5.110815137197631530e-02],\
      [-3.611115086978421845e-02,-3.801763758666952542e-02,-4.019050114086200609e-02,-3.471794303430733586e-02],\
      [2.441437672883787005e-02,2.512218135148977169e-02,2.611569010908706620e-02,2.690613802224062212e-02],\
      [-9.467030727773922960e-02,-9.669395401624621134e-02,-9.782062073557150350e-02,-9.732596561318529460e-02],\
      [-2.191670036729810589e-02,-2.268360195641114241e-02,-2.372367110938786508e-02,-2.015361185588398357e-02],\
      [3.875923789194093971e-02,4.127701022023270300e-02,4.158819720251302060e-02,4.094502955835392644e-02],\
      [-1.063579548566755129e-02,-1.317134199372879330e-02,-1.305969919121760525e-02,-1.172806553141964719e-02],\
      [5.846661668172203896e-02,5.965585360273819443e-02,5.976871208148410580e-02,5.792273556007334484e-02],\
      [4.383750777887278349e-02,4.329993418822790374e-02,4.390834286714637852e-02,4.162432450703226761e-02],\
      [5.303700335028108809e-02,5.326246153160257846e-02,5.213511208379328216e-02,5.140960216414366957e-02],\
      [-1.308617368681529343e-02,-1.216846877814960724e-02,-1.132702216305610590e-02,-1.485433911142607089e-02],\
      [1.316120825165866155e-02,1.396309952774785895e-02,1.696701963714668943e-02,1.967479064347872272e-02],\
      [-5.310212171025585626e-02,-5.311972633825521456e-02,-5.441096634803904014e-02,-5.160461593333538766e-02],\
      [1.292684503301703633e-02,1.237450870379510834e-02,1.337136046731622271e-02,1.542101972063633988e-02],\
      [-8.315035525881275813e-02,-8.299955687262056125e-02,-8.004561641951067619e-02,-7.470481987662977441e-02],\
      [-7.863307985612544293e-02,-7.863319491098236247e-02,-8.013725469330143514e-02,-7.902097309013970949e-02],\
      [2.355240456682399300e-02,2.219648812694692205e-02,2.206858385596189437e-02,2.464753259564310406e-02],\
      [3.562505119202603182e-02,3.538363846949490327e-02,3.625876398572648596e-02,3.235336364761568634e-02],\
      [-5.739109462606805517e-02,-5.938647313370800512e-02,-6.214423298102277060e-02,-6.355055089000388735e-02],\
      [9.245441717637169817e-04,2.101445489500121389e-03,2.493517714957893018e-03,2.423004591004564168e-03],\
      [-3.992525745803518359e-04,-2.005049792043855916e-03,-1.291346252408969017e-03,9.437591529705803908e-04],\
      [1.390168065837252623e-02,1.674588064840331486e-02,1.732587005104446395e-02,1.208107021572321985e-02],\
      [-2.904140726292027061e-02,-2.890164444392384624e-02,-2.995102749872341832e-02,-2.724562003767830656e-02],\
      [-8.833787899343954406e-03,-1.037639884954125007e-02,-1.110291545730161637e-02,-9.999707427901858084e-03],\
      [4.252711244509083804e-02,4.221503420714246141e-02,4.068945280374444695e-02,3.500800278478218008e-02],\
      [-8.880863243257449248e-04,-8.019748793115205176e-04,-7.602464503207241901e-04,-7.776263108465329872e-04],\
      [-4.519736229672230779e-03,-4.396784797144812768e-03,-4.236446946909271961e-03,-4.154750060246936369e-03],\
      [1.440909240243171824e-02,1.450017826669973420e-02,1.480774134741435696e-02,1.513091298916856113e-02],\
      [3.011232590999694033e-03,3.152992813285312654e-03,3.078260946170720963e-03,2.544627031911187928e-03],\
      [4.056730802681312838e-05,-2.251811290259288006e-04,-3.645543669710108771e-04,2.782056364411475695e-04],\
      [-9.234649012414958974e-03,-9.169990590783785867e-03,-9.354914402375274357e-03,-9.915519277118046634e-03],\
      [-2.158561856532133227e-03,-2.425898887041384906e-03,-2.406708581017268176e-03,-1.689938633151443371e-03],\
      [-2.638051378725561852e-04,-2.289990226241337074e-04,-1.726596133562415306e-04,-3.370430105492127943e-04],\
      [1.910436974283502673e-04,2.427159629751297681e-04,1.944607774018277313e-04,3.412206259488409260e-05],\
      [-4.503756878885410014e-03,-4.639567546164078196e-03,-4.833198682350828973e-03,-5.131495336156883386e-03],\
      [-1.660122681100343819e-02,-1.737897028119927273e-02,-1.655390225470840596e-02,-1.781919787987515727e-02],\
      [2.479633791586743387e-03,1.207654899843806735e-03,2.054124650019108472e-03,2.013717087637206023e-03],\
      [3.764612942593648093e-02,3.930709439224980284e-02,3.791546842599128470e-02,3.658844084870323948e-02],\
      [-4.706837498705624713e-03,-4.943599982964972349e-03,-5.460249471037776844e-03,-3.815948404518826852e-03],\
      [2.874315747983649527e-02,3.049759838180319399e-02,3.137103918592903939e-02,3.054971390083463523e-02],\
      [3.535797791522082845e-02,3.684823310415592107e-02,3.820108567590276005e-02,3.746002407076440971e-02],\
      [-3.741701848530692293e-02,-3.857840654789151252e-02,-3.923914826495443486e-02,-3.631697779812077809e-02],\
      [-1.314139702756494943e-02,-1.316915370968656240e-02,-1.270957704829486952e-02,-1.055670149348792580e-02],\
      [-1.002514883953385672e-02,-1.022688612552927027e-02,-1.072290213826015623e-02,-1.297775018471336930e-02],\
      [-7.423271219472414584e-03,-8.143085235244812772e-03,-9.219139540650730241e-03,-1.057865724202803302e-02],\
      [sumToOneWeight, sumToOneWeight, sumToOneWeight, sumToOneWeight]]),
            '2014_07_23': numpy.array(
        [[-5.464290336540255505e-02,-5.767020445924114780e-02,-5.906110955304696292e-02,-6.700504667505242928e-02],
        [-5.115107950026569900e-02,-5.409355725777687668e-02,-5.342280766935707248e-02,-5.469063156575638962e-02],
        [-3.644368840331627807e-02,-2.628599911733342509e-02,-2.854726863619490643e-02,-3.228408727634863445e-02],
        [-1.845139979305272099e-02,4.582986066437087433e-03,-9.796145860438624890e-04,3.198099331919701180e-03],
        [-1.052405869706085767e-01,-9.502217271616275607e-02,-9.963857788261415438e-02,-1.089589302578710950e-01],
        [-9.441819322575252527e-02,-5.964566254748319973e-02,-6.544315525177371584e-02,-7.866664388080202297e-02],
        [-1.535890065317412762e-02,-1.096202220956716926e-02,-5.954946972867429002e-03,2.002366659560623346e-04],
        [-5.344756256346760992e-02,-1.912294568596969654e-02,-2.184813581617991995e-02,-2.334481581880084450e-02],
        [-5.853352518392838932e-02,-2.886462434435403679e-03,-1.223467037213730665e-02,3.823838584255143808e-03],
        [1.950779216732365096e-02,-3.115666387579302862e-03,3.116027529538804245e-03,-4.913956702173007812e-03],
        [3.722839187043883169e-02,1.196436181371859919e-02,1.514068506501519210e-02,8.639824338943528567e-03],
        [8.827592367138858975e-02,7.598319207923980023e-02,7.513388986981874018e-02,7.866025549503966041e-02],
        [5.127496970571243651e-02,7.391908596242074969e-02,7.150301777473304365e-02,4.379848836501164244e-02],
        [4.104605726014266820e-02,-6.681898377728911001e-03,-3.350170067917183567e-03,-2.230394927494897331e-02],
        [1.878685690229944527e-01,1.691250215929575862e-01,1.855592999574983137e-01,1.645648690359144128e-01],
        [1.183840044858385787e-01,9.587359594411411223e-02,1.037224797415067651e-01,9.057911763157400209e-02],
        [2.065272812765595600e-01,1.735393267016661356e-01,1.766126764763210621e-01,1.869085404855105603e-01],
        [2.527335758405409305e-02,9.532930377039894321e-03,1.560974909032925712e-02,2.465819749710248046e-02],
        [7.765629706610430172e-02,7.376525410464453147e-02,7.781371707749906719e-02,8.646642457248507330e-02],
        [-5.159366536498603828e-02,-4.386522480345243780e-02,-5.790013529858453745e-02,-5.342514056053505878e-02],
        [3.096206626847060675e-02,2.817342567332670536e-02,2.803040322252116703e-02,8.159928154395458544e-03],
        [-7.274664797894490886e-02,-7.883449637151143663e-02,-8.686136847593858845e-02,-7.671703245050162656e-02],
        [-2.620261220391492327e-02,-3.525057461175230139e-02,-2.951452114357644083e-02,-1.523746678296718920e-02],
        [7.267773933404807207e-02,2.907584207722927611e-02,5.033184227128905536e-02,6.975625560526513280e-02],
        [-2.521902668462255512e-02,8.795990991494615635e-03,1.654159957000518209e-03,1.548064559550171165e-02],
        [-3.141512588668788492e-02,8.752777779304117545e-03,5.870538132721337191e-03,3.324994630397553989e-03],
        [1.610572363156139927e-03,-7.660859390263171503e-03,-2.346704478512865420e-03,-1.677557820685602816e-02],
        [7.940188302396607167e-02,5.238370811946130995e-02,4.752624499791829882e-02,5.845021570747249012e-02],
        [-8.305333205688321396e-02,-8.740353995670634146e-02,-8.663206867035706804e-02,-8.962243859214236164e-02],
        [-3.134459925376070211e-01,-2.919590542175634629e-01,-2.982909888998974135e-01,-2.881066639395697959e-01],
        [-1.320436513210617446e-01,-8.106065659799134571e-02,-9.040166438215160860e-02,-7.102633870143021388e-02],
        [9.141627919282124815e-02,3.741983845073103970e-02,4.302319368486359763e-02,5.346957292034752035e-02],
        [6.531423423903673364e-02,4.173879306464137184e-03,1.315499774664568439e-02,2.540795330849436595e-03],
        [-2.512167249071487474e-01,-2.293017651229115328e-01,-2.308316107272400108e-01,-2.296341049497438447e-01],
        [7.854083128657096680e-02,1.322086447508264151e-01,1.200017405701558487e-01,1.301844883787950380e-01],
        [1.348043454256773327e-02,2.324465342745282020e-02,2.193953217717072718e-02,2.098828508558031256e-02],
        [2.211031106873930646e-02,8.039814115773015468e-03,1.377479441282658708e-02,2.396621041068460606e-02],
        [2.565339333505840813e-03,-2.957788837729030326e-02,-2.598407384951788301e-02,-4.176198317761675716e-02],
        [-1.561390900549435024e-02,-6.959716041897632405e-03,-7.563711192607475847e-03,2.578537985645889229e-03],
        [-4.715632795774485353e-02,-3.922153971939058847e-02,-4.066009260414800430e-02,-4.262055569914211667e-02],
        [3.944868046722410648e-02,7.843136962646812815e-02,7.306767876345292290e-02,7.781037952994351858e-02],
        [-1.305191272114236516e-02,-3.333090362074655338e-02,-3.117440559557061591e-02,-3.399503540879177804e-02],
        [-5.878963125418451563e-02,-4.746036917258404653e-02,-5.138968658059000355e-02,-4.655383008471902090e-02],
        [3.517935140482630896e-02,4.339498921404126575e-02,4.047724978415100094e-02,2.944767940518291591e-02],
        [-1.419711165578261408e-02,-2.600311235119719469e-02,-2.403528122336769449e-02,-2.231501555809822096e-02],
        [4.673631963007365830e-02,4.222122860493134067e-02,4.051900184392275006e-02,2.429042580682045163e-02],
        [4.698390687205909744e-02,2.801285273380542742e-02,2.785620535881803625e-02,1.345851306437251954e-02],
        [6.088456957907769501e-02,5.617267756739811879e-02,6.172067025414008229e-02,6.769326202579863117e-02],
        [4.844879695570007694e-02,5.740838066700899855e-02,5.886020855683895409e-02,5.301874908051096291e-02],
        [1.384848789077177678e-01,1.769173528968090436e-01,1.691611951419131621e-01,1.742668314353199854e-01],
        [4.053052385681649161e-02,3.012822603078371686e-02,3.839254235447352170e-02,4.390007708776469397e-02],
        [6.925080147411756537e-03,5.572545235147760567e-02,4.636146390010906226e-02,4.502929061198106264e-02],
        [-7.227781819370950045e-02,-6.763510172663662889e-02,-7.217489552309069856e-02,-7.282333914396818542e-02],
        [-1.008287344909177680e-01,-8.889299472103404098e-02,-9.055437899463497642e-02,-1.072965907866354346e-01],
        [-9.736956896355325464e-02,-1.353523652443247294e-01,-1.352381115496958108e-01,-1.243509360270547565e-01],
        [-8.004713198776981092e-03,-1.556205882857981601e-02,-3.684195079664918937e-02,-3.137802688610195900e-02],
        [-1.043843225835274641e-01,-1.138555287821729628e-01,-8.735718508239048719e-02,-6.512854117530177123e-02],
        [-1.023930949318214573e-01,-9.762016258570074823e-02,-9.173794000587955078e-02,-9.828225044298957713e-02],
        [-7.015927946292823542e-03,5.161269524257226793e-02,3.910941472153854626e-02,3.351430048608956130e-02],
        [sumToOneWeight, sumToOneWeight, sumToOneWeight, sumToOneWeight]]),
               }.get(instr, 'Error')

    if help:
        print('Available dates for the endmember versions are:')
        print('2009_08_10')
        print('2012_12_07')
        print('2013_01_08')
        print('2014_07_23')

        return

    sum_to_one_weight = sum_weight(date)

    endmembers = get_endmembers(date, sumToOneWeight=sum_to_one_weight)

    return endmembers


class EndMember(object):

    def __init__(self, id, componentNames, values, sumWeight):
        self.id = id
        self.componentNames = componentNames
        self.values = values
        self.sumWeight = sumWeight
       
class EndMemberFactory(object):

    _WEIGHTS_AND_NAMES = {
        '2013_01_08' : {'weight': 0.02, 'components':('green', 'dead1', 'dead2', 'bare')},
        '2012_12_07' : {'weight': 0.02, 'components':('green', 'dead', 'bare1', 'bare2')},
        '2009_08_10' : {'weight': 0.01, 'components':('green', 'dead', 'bare1', 'bare2')},
        '2014_07_23' : {'weight': 1.0, 'components':('green', 'dead', 'bare1', 'bare2')}
    }


    @staticmethod
    def getAllIds():
        return EndMemberFactory._WEIGHTS_AND_NAMES.keys()

    @staticmethod
    def getEndMemberById(id):
        sumWeight = EndMemberFactory._WEIGHTS_AND_NAMES[id]['weight']
        componentNames = EndMemberFactory._WEIGHTS_AND_NAMES[id]['components']
        values = endmember_version(id)

        return EndMember(id, componentNames, values, sumWeight)
