# This file was automatically created by FeynRules 1.6.11
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (February 23, 2011)
# Date: Mon 15 Sep 2014 21:33:43


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec



GC_1 = Coupling(name = 'GC_1',
                value = 'cLBh*complex(0,1)',
                order = {'LBh':1})

GC_2 = Coupling(name = 'GC_2',
                value = 'cLTh*complex(0,1)',
                order = {'LTh':1})

GC_3 = Coupling(name = 'GC_3',
                value = 'cRBh*complex(0,1)',
                order = {'RBh':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'cRTh*complex(0,1)',
                order = {'RTh':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '(-4*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = '(5*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(8*ee*complex(0,1))/3.',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_14 = Coupling(name = 'GC_14',
                 value = 'cw*complex(0,1)*gw',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(complex(0,1)*gw**2)',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = 'cw**2*complex(0,1)*gw**2',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(cLVW*ee**2*complex(0,1))/(2.*LAMBDA*sw**2)',
                 order = {'LVW':1,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(cRVW*ee**2*complex(0,1))/(2.*LAMBDA*sw**2)',
                 order = {'QED':2,'RVW':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(CKM11*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(CKM12*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(CKM13*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(CKM21*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(CKM22*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(CKM23*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(CKM31*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(CKM32*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(CKM33*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(cLBW*ee*complex(0,1))/(2.*sw)',
                 order = {'LBW':1,'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(cLBZ*ee*complex(0,1))/(2.*sw)',
                 order = {'LBZ':1,'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(cLTW*ee*complex(0,1))/(2.*sw)',
                 order = {'LTW':1,'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cLTZ*ee*complex(0,1))/(2.*sw)',
                 order = {'LTZ':1,'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cLXW*ee*complex(0,1))/(2.*sw)',
                 order = {'LXW':1,'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(cLYW*ee*complex(0,1))/(2.*sw)',
                 order = {'LYW':1,'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cRBW*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1,'RBW':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(cRBZ*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1,'RBZ':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cRTW*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1,'RTW':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(cRTZ*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1,'RTZ':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cRXW*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1,'RXW':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cRYW*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1,'RYW':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = 'complex(0,1)*gw*sw',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-2*cw*complex(0,1)*gw**2*sw',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = 'complex(0,1)*gw**2*sw**2',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-6*complex(0,1)*lam*v',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(ee**2*complex(0,1)*v)/(2.*sw**2)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = 'ee**2*complex(0,1)*v + (cw**2*ee**2*complex(0,1)*v)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*v)/(2.*cw**2)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee*complex(0,1)*complexconjugate(CKM11))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee*complex(0,1)*complexconjugate(CKM12))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(ee*complex(0,1)*complexconjugate(CKM13))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(ee*complex(0,1)*complexconjugate(CKM21))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(ee*complex(0,1)*complexconjugate(CKM22))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(ee*complex(0,1)*complexconjugate(CKM23))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(ee*complex(0,1)*complexconjugate(CKM31))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(ee*complex(0,1)*complexconjugate(CKM32))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(ee*complex(0,1)*complexconjugate(CKM33))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

