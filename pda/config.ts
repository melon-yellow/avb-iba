/*
    Iba PDA Config.IO
*/

// Valid Tag Regex
export const tagRegex = /([0-9]+)((.|:){1})([0-9]+)/

// File Interface
export interface Config {
    IOConfiguration: {
        Modules: Module[]
    }
}

export interface Module {
    Name: string
    ModuleType: number
    Enabled: boolean
    ModuleNr: number
    FileModuleNr?: number
    NrAnalogSignals: number
    NrDigitalSignals: number
    Links: Link[]
    CPUName?: string
    PCCP_Destination?: string
}

export interface Link {
    Analog: Signal[]
    Digital: Signal[]
}

export interface Signal {
    Name: string
    DataType: number
    Active: boolean
    Unit?: string
    Comment1?: string
    Comment2?: string
    Expression?: string
    FileSignalId?: string
    S7Symbol?: string
    S7Operand?: string
    S7DataType?: string
}

// Get Module By Number
export const getModuleByNumber = (config: Config, nr: number) => {
    for (const module of config.IOConfiguration.Modules) {
        if (module?.FileModuleNr == nr) return module
        else if (module.ModuleNr == nr) return module
    }
}

// Get Signal By Tag
export const getSignalByTag = (config: Config, tag: string) => {
    if (!tagRegex.test(tag)) throw new Error('invalid tag')
    const alog = tag.includes(':')
    const tagType = alog ? 'Analog' : 'Digital'
    const [mod, index] = alog ? tag.split(':') : tag.split('.')
    return getModuleByNumber(config, Number(mod))
        ?.Links[0][tagType][Number(index)]
}
