library(DSS)
args = commandArgs(trailingOnly=TRUE)

###############################################################

#Cov <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region_Cov.txt",header=T,sep="\t",check.names=FALSE))
#M <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region_M.txt",header=T,sep="\t",check.names=FALSE))
#Loci <- read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region.info.txt",header=T,sep="\t",check.names=FALSE)
#bs.combine.filtered <- BSseq(chr = Loci$chr, pos = Loci$start , M = M, Cov = Cov, sampleNames = colnames(M))

bs.combine.filtered <- readRDS(args[1])
###do not change#############################################################
macaq.ind <- sampleNames(bs.combine.filtered)[grep("YN",sampleNames(bs.combine.filtered))]
human.ind <-sampleNames(bs.combine.filtered)[grep("Control",sampleNames(bs.combine.filtered))]
chimp.ind <- sampleNames(bs.combine.filtered)[!(sampleNames(bs.combine.filtered) %in% c(human.ind,macaq.ind))]
covariates_R <- read.table("../../bsseq/matrix/covariates_all.txt",header=T)
row.names(covariates_R) <- covariates_R$GT_ID

####################################################################

###########

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.combine.filtered)),])
covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.combine.filtered)$CellType <- covariates_R_order$CellType
pData(bs.combine.filtered)$Species <- covariates_R_order$Species
pData(bs.combine.filtered)$Sex <- covariates_R_order$Sex
pData(bs.combine.filtered)$Age_Class <- covariates_R_order$Age_Class
pData(bs.combine.filtered)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.combine.filtered)<- droplevels(pData(bs.combine.filtered))
pData(bs.combine.filtered)$Species <- factor(pData(bs.combine.filtered)$Species, levels = c("Human", "Chimp", "Macaque"))

##################

#model.matrix(~Species+CellType+Sex+Age_Class+Conversion_rates+Species:CellType,pData(bs.PR.olig))
#SpeciesHuman SpeciesMacaque CellTypeOlig SpeciesHuman:CellTypeOlig


###############

DMLfit = DMLfit.multiFactor(bs.combine.filtered,pData(bs.combine.filtered), ~Species+Sex+Age_Class+Conversion_rates)
contrast_matrix <- matrix(c(0,1,-1,0,0,0,0), ncol=1)
DMLtest = DMLtest.multiFactor(DMLfit, Contrast=contrast_matrix)
write.table(DMLtest,file=paste0(args[2],"_Species_HvsCM.txt"),sep="\t",row.names=F,quote=F)
DMRtest <- callDMR(DMLtest, p.threshold=0.005)
write.table(DMRtest,file=paste0(args[2],"_Species_HvsCM.DMR.txt"),sep="\t",row.names=F,quote=F)

##############






