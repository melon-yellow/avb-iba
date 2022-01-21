
##########################################################################################################################

# Imports
from json import dumps
from typing import TypedDict

##########################################################################################################################

class IPrevent(TypedDict):
    master: tuple[str,str]
    area: 'IPreventAreas'

class IPreventAreas(TypedDict):
    CTR: tuple[str,str,str,str,str,str]
    MIL: tuple[str,str,str,str,str,str]
    ROD: tuple[str,str,str,str]
    RAX: tuple[str,str,str,str]
    VCH: tuple[str,str]
    COL: tuple[str,str]
    BARH: tuple[str,str,str,str]

##########################################################################################################################
#                                                   PDA MILL STATUS CAUSE                                                #
##########################################################################################################################

# Get General Cause
def cause(
    data: IPrevent,
    status: str
):
    # Check Index
    if not 'master' in data: return ''
    if not isinstance(data['master'], list): return ''
    if not 'area' in data: return ''
    if not isinstance(data['area'], dict): return ''
    if len(data['master']) != 2: return ''

    # All Areas
    areas = {
        'CTR': ['RM','IM','FM'],
        'MIL': ['RM','IM','FM'],
        'ROD': ['WR','STELM'],
        'RAX': ['WR','STELM'],
        'VCH': ['CH'],
        'COL': ['COOL'],
        'BARH': ['BARH','STACK']
    }

    # Check PLCs
    plcsr = list(areas.keys())
    plcs = list(data['area'].keys())
    if (dumps(plcsr) !=
        dumps(plcs)): return ''

    # Check Areas
    for p in plcs:
        if not isinstance(data['area'][p], list): return ''
        if len(data['area'][p]) != (len(areas[p]) * 2): return ''

    # Get Cause Text
    text = ''
    if status == 'gap_off': text = data['master'][0]
    if status == 'cobble': text = data['master'][1]
    if text == '': return ''

    # Iter 16 Times
    for r in range(16):
        # Iter Over PLCs
        brk = False
        for p in areas:
            plc = areas[p]
            # Iter Over Areas 
            for area in plc:
                i = -1
                if text == f'<{p}/{area}/SB>': i = len(plc)
                if text == f'<{p}/{area}/PB>': i = 0
                if i < 0: continue
                # Update Text
                a = plc.index(area)
                text = '' + data['area'][p][a + i]
                brk = True
                break
            # Check Break
            if brk: break
        # Check Full Break
        if not brk: break

    # Return Text
    return text

##########################################################################################################################
