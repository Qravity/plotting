from abc import ABCMeta, abstractmethod

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc("figure", facecolor="white")  # remove gray background

class Plot2D(object):
	""" A simple 2D plotting wrapper class with basic style
		All the figures are overlaid in one panel
	
	Attribute:
		x:
		y:
		xlabel:
		ylabel:
	"""
	
	@staticmethod
	def show():
		plt.show()
	
	def __init__(self,x, y, xlabel='',ylabel=''):
		"""Return a new 2D figure objects"""
		self.x = x
		self.y = y
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.fig = plt.figure()
		self.axarr = self.fig.add_subplot(111)
				
	def set_style(self):
		"""Set axis and style"""
		self.axarr.set_xlabel(self.xlabel, fontsize=15)
		self.axarr.set_ylabel(self.ylabel, fontsize=15)
		self.axarr.xaxis.set_label_coords(0.5, -0.05)
		self.axarr.yaxis.set_label_coords(-0.1, 0.5)
			
	def set_legend(self, legend=''):
		"""Set legend"""
		self.legend = legend
		
	def set_min_max(self):
		"""Set min, max for displayig"""
		xmin = 0.25*min(self.x)
		xmax = 1.25*max(self.x)
		ymin = 0.25*min(self.y)
		ymax = 1.25*max(self.y)
		self.axarr.set_xlim([xmin, xmax])
		self.axarr.set_ylim([ymin, ymax])
		
	def tight_layout(self):
		"""Tight layout"""
		self.fig.tight_layout()
	
	@abstractmethod
	def plot(self):
		pass
		

class PointPlot2D(Plot2D):
	"""2D plot of points"""
	def plot(self):
		self.axarr.plot(self.x, self.y, 'ro')


class LinePlot2D(Plot2D):
	"""2D plot of line"""
	def plot(self):
		self.axarr.plot(self.x, self.y, 'b-', label=self.legend, linewidth=1)
		self.axarr.legend(loc='lower right')	


class PointPlot2DErr(Plot2D):
	"""2D plot of points with error"""

	def set_error(self, xerr, yerr):
		"""Adding error attributes"""
		self.xerr = xerr
		self.yerr = yerr 

	def plot(self):
		self.axarr.errorbar(self.x, self.y, xerr=self.xerr, yerr=self.yerr, fmt='ro', markeredgewidth=1, ecolor='black')

class ScatterPlot2D(Plot2D):
	"""2D plot of scatter"""
	def plot(self):
		self.axarr.scatter(self.x, self.y, 'ro')	
	
	