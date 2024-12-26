class LightHouseReport:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def get_version() -> str:
        return self.data['lighthouseVersion']

    def get_domain(self) -> str:
        return self.data['requestedUrl']

    def report_date(self) -> str:
        return self.data['fetchTime']

    def audits(self, key: str) -> dict:
        if 'audits' in self.data and key in self.data['audits']:
            return self.data['audits'][key]
        else:
            return {"error": "key is not present in the data"}

    @property
    def is_https(self) -> dict:
        return self.audits('is-on-https')

    @property
    def redirects_http(self)-> dict:
        return self.audits('redirects-http')

    @property
    def viewport(self)-> dict:
        return self.audits('viewport')

    
    

