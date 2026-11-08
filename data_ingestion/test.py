from laod_target import LoadTarget
from load_training import LoadTraining

loaderx = LoadTraining()
loadery = LoadTarget()

loaderx.load_data(
    r"E:\FU Berlin Masters\Semester 3\Life Science Project\workspace\AdamsonWeissman2016_GSM2406681_10X010.h5ad"
)
loadery.load_data(r"C:\Users\dell\Desktop\prices_key.csv")

print(loaderx.adata.obs)
print(loadery.data.shape)
