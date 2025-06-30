class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(NotVaccinatedError):
    pass


class NotWearingMaskError(Exception):
    pass
