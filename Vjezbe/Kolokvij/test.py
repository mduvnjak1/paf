import ProjectileDrop as pd
import numpy as np
import matplotlib.pyplot as plt
p1=pd.ProjectileDrop()
p1.set_initial_conditions_potvrda(200,0,2000)
p2=pd.ProjectileDrop()
p2.set_initial_conditions_potvrda(20,0,500)
p2.promjena_visine(50)
p2.promjena_brzine_x_za_iznos_dv(5)
p1.plot_x_y()
p1.plot_vy_t()
p1.plot_total_time_dt(0.001,0.1,0.001)
print(p1.time_to_hit_target(20000,50,50))