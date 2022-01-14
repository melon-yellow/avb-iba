
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
    Unit: string
    Active: boolean
    Expression: string
}
