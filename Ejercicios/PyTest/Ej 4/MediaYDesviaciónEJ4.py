class MediayDesviación():
    def calculate_statistics(self,list):
        med = sum(list) / len(list)
        var  = sum([((x - med) ** 2) for x in list]) / len(list)
        desv  = var ** 0.5

        return med, desv

    
