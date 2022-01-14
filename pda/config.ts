
type XML = {
    IOConfiguration: {
        Modules: Module[]
    }
}

type Module = {
    Name: string
    ModuleNr: string
    Links: Link[]
}

type Link = {
    Analog: Signal[]
    Digital: Signal[]
}

type Signal = {
    Name: string
    DataType: number
    Active: boolean
    Unit?: string
    Expression?: string
    FileSignalId?: string
}

const tagRegex = /([0-9]+)((.|:){1})([0-9]+)/
const tagExample = '14:4'
const tagNameExample = 'STD15 M_ACT'