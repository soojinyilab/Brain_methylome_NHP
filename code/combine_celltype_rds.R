library(DSS)
args = commandArgs(trailingOnly=TRUE)
bs.ND <- readRDS(args[1])
bs.OD <- readRDS(args[2])

bs.combine.filtered <- combine(bs.ND,bs.OD)

macaq.ind <- sampleNames(bs.combine.filtered)[grep("YN",sampleNames(bs.combine.filtered))]
macaq.ind.neun <- macaq.ind[grep("_ND",macaq.ind)]
macaq.ind.olig <- macaq.ind[grep("_OD",macaq.ind)]

human.ind <-sampleNames(bs.combine.filtered)[grep("Control",sampleNames(bs.combine.filtered))]
human.ind.neun <- human.ind[grep("_NeuN",human.ind)]
human.ind.olig <- human.ind[grep("_Olig2",human.ind)]

chimp.ind <- sampleNames(bs.combine.filtered)[!(sampleNames(bs.combine.filtered) %in% c(human.ind,macaq.ind))]
chimp.ind.neun <- chimp.ind[grep("_ND",chimp.ind)]
chimp.ind.olig <- chimp.ind[grep("_OD",chimp.ind)]


bs.cov <- getCoverage(bs.combine.filtered,type="Cov")
min.cov <- 5
ind.per <- 0.5
bs.good.loci <- which(rowSums(bs.cov[,human.ind.neun] >= min.cov) >= 5 & rowSums(bs.cov[,human.ind.olig] >= min.cov) >= 5 & rowSums(bs.cov[,chimp.ind.neun] >= min.cov) >= 5 & rowSums(bs.cov[,chimp.ind.olig] >= min.cov) >= 5 & rowSums(bs.cov[,macaq.ind.neun] >= min.cov) >= 5 & rowSums(bs.cov[,macaq.ind.olig] >= min.cov) >= 5)
bs.combine.filtered <- bs.combine.filtered[bs.good.loci,]
saveRDS(bs.combine.filtered, file = args[3])

