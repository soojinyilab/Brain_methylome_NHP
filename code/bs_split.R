library(DSS)
args = commandArgs(trailingOnly=TRUE)

###############################################################

#Cov <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region_Cov.txt",header=T,sep="\t",check.names=FALSE))
#M <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region_M.txt",header=T,sep="\t",check.names=FALSE))
#Loci <- read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region.info.txt",header=T,sep="\t",check.names=FALSE)
#bs.combine.filtered <- BSseq(chr = Loci$chr, pos = Loci$start , M = M, Cov = Cov, sampleNames = colnames(M))

bs.combine <- readRDS(args[1])
###do not change#############################################################
human.ind <-sampleNames(bs.combine)[grep(args[2],sampleNames(bs.combine))]
chimp.ind <- sampleNames(bs.combine)[grep(args[3],sampleNames(bs.combine))]
bs.combine <- bs.combine[,c(human.ind,chimp.ind)]

####################################################################

bs.cov <- getCoverage(bs.combine,type="Cov")
min.cov <- 3
ind.per <- 0.5
bs.good.loci <- which(rowSums(bs.cov[,human.ind] >= min.cov) >= round(length(human.ind)*ind.per,0) & rowSums(bs.cov[,chimp.ind] >= min.cov) >= round(length(chimp.ind)*ind.per,0))
bs.combine.filtered <- bs.combine[bs.good.loci,]
bs.chr<- chrSelectBSseq(bs.combine.filtered, seqnames = args[4], order = TRUE)
saveRDS(bs.chr,file=args[5])

#saveRDS(bs.neun.cont.filtered, file = "bs_neun_cont_chimp_filtered.rds")

#bs.olig.good.loci <- which(rowSums(bs.olig.cont.cov[,control.ind.olig] >= min.cov) >= round(length(control.ind.olig)*ind.per,0) & rowSums(bs.olig.cont.cov[,chimp.ind.olig] >= min.cov) >= round(length(chimp.ind.olig)*ind.per,0))
#bs.olig.cont.filtered <- bs.olig.cont[bs.olig.good.loci,]
#saveRDS(bs.olig.cont.filtered, file = "bs_olig_cont_chimp_filtered.rds")
#################################################################################################################

#bs.neun.cont.filtered <- readRDS("bs_neun_cont_chimp_filtered.rds")
#bs.olig.cont.filtered <- readRDS("bs_olig_cont_chimp_filtered.rds")
#min.cov <- 10
#ind.per <- 0.8

#control.ind.neun <- sampleNames(bs.neun.cont.filtered)[grep("Control",sampleNames(bs.neun.cont.filtered))]
#control.ind.olig <- sampleNames(bs.olig.cont.filtered)[grep("Control",sampleNames(bs.olig.cont.filtered))]
#chimp.ind.neun <- sampleNames(bs.neun.cont.filtered)[!(sampleNames(bs.neun.cont.filtered) %in% control.ind.neun)]
#chimp.ind.olig <- sampleNames(bs.olig.cont.filtered)[!(sampleNames(bs.olig.cont.filtered) %in% control.ind.olig)]


#bs.combine<- combineList(bs.neun.cont.filtered,bs.olig.cont.filtered)
#bs.combine.cov <- getCoverage(bs.combine,type="Cov")
#bs.combine.good.loci <- which(rowSums(bs.combine.cov[,control.ind.neun] >= min.cov) >= round(length(control.ind.neun)*ind.per,0) & rowSums(bs.combine.cov[,chimp.ind.neun] >= min.cov) >= round(length(chimp.ind.neun)*ind.per,0) & rowSums(bs.combine.cov[,chimp.ind.olig] >= min.cov) >= round(length(chimp.ind.olig)*ind.per,0) & rowSums(bs.combine.cov[,control.ind.olig] >= min.cov) >= round(length(control.ind.olig)*ind.per,0))
#bs.combine.filtered <- bs.combine[bs.combine.good.loci,] 
#saveRDS(bs.combine.filtered, file = "dd_bs_combine_neun_olig_cont_chimp_filtered.rds")

#sub.loci <-granges(bs.combine.filtered)
#sub.meth <-getMeth(bs.combine.filtered,type="raw")
    
#write.table(format(sub.meth, digits=3),file="bs_filtered_10_cont_chimp_meth.txt",sep="\t",row.names=F,quote=F)
#write.table(sub.loci,file="bs_filtered_10_cont_chimp_loci.txt",sep="\t",row.names=F,quote=F)


