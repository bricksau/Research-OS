# ==============================================================================
# Research-OS: 300 DPI 出版级学术图表 ggplot2 主题规范
# ==============================================================================

suppressPackageStartupMessages({
  if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
  library(ggplot2)
})

theme_publication <- function(base_size = 11, base_family = "sans") {
  theme_minimal(base_size = base_size, base_family = base_family) %+replace%
    theme(
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "#e5e7eb", linewidth = 0.5),
      axis.line = element_line(color = "#374151", linewidth = 0.6),
      axis.ticks = element_line(color = "#374151", linewidth = 0.5),
      axis.title = element_text(face = "bold", size = rel(1.0), color = "#111827"),
      axis.text = element_text(size = rel(0.9), color = "#374151"),
      plot.title = element_text(face = "bold", size = rel(1.2), hjust = 0, margin = margin(b = 8)),
      plot.subtitle = element_text(size = rel(0.95), color = "#4b5563", margin = margin(b = 10)),
      legend.position = "bottom",
      legend.title = element_text(face = "bold", size = rel(0.9)),
      legend.text = element_text(size = rel(0.85))
    )
}

# 导出函数包装：严格保证 300 DPI 与物理尺寸
export_figure <- function(plot_obj, filename, width_in = 7.0, height_in = 4.5) {
  ggsave(
    filename = filename,
    plot = plot_obj,
    width = width_in,
    height = height_in,
    dpi = 300,
    units = "in"
  )
  message(paste0("✅ 已导出 300 DPI 学术图表: ", filename))
}
