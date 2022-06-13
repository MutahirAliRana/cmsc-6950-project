import pandas as pd

class Transformer:
    def __init__(self, transformed, raw):
        self.df_t = transformed
        self.df_r = raw

    def clean(self):
        code = self.df_t["CODE"].unique().tolist()
        country = self.df_t["COUNTRY"].unique().tolist()
        hdi = []
        tc = []
        t_d = []
        sti = []
        population = self.df_t["POP"].unique().tolist()

        for i in country:
            hdi.append(
                (self.df_t.loc[self.df_t["COUNTRY"] == i, "HDI"]).sum()/294)
            tc.append(
                (self.df_r.loc[self.df_r["location"] == i, "total_cases"]).sum())
            t_d.append(
                (self.df_r.loc[self.df_r["location"] == i, "total_deaths"]).sum())
            sti.append(
                (self.df_t.loc[self.df_t["COUNTRY"] == i, "STI"]).sum()/294)
            population.append(
                (self.df_r.loc[self.df_r["location"] == i, "population"]).sum()/294)

        aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, t_d, sti, population)),
                                       columns=["Country Code", "Country", "HDI",
                                                "Total Cases", "Total Deaths",
                                                "Stringency Index", "Population"])
        return aggregated_data
    
    def add_entropy(self, df):
      data = df.head(10)
      data["GDP Before Covid"] = [65279.53, 8897.49, 2100.75,
                                  11497.65, 7027.61, 9946.03,
                                  29564.74, 6001.40, 6424.98, 42354.41]
      data["GDP During Covid"] = [63543.58, 6796.84, 1900.71,
                                  10126.72, 6126.87, 8346.70,
                                  27057.16, 5090.72, 5332.77, 40284.64]
      return data
