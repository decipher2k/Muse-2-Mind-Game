# Explicit is better than implicit
from godot import exposed, export, Vector2, Node2D, Vector3, Node, ResourceLoader
from pylsl import StreamInlet, resolve_stream 
from os import system, name

@exposed
class Rock(Node):
		THRESHHOLD=0
		streams=0
		inlet=0
		count=0
		max=0
		sum=0
		sample=0
		timestamp =0
		_max=0
		_error=False
		_ready=False
		# Can export property as well
		@export(int)
		@property
		def age(self):
				return self._age

		@export(bool)
		@property
		def error(self):
				return self._error
				
		@export(bool)
		@property
		def ready(self):
				return self._ready				
				
		@export(float)
		@property
		def threshholdlevel(self):
				return self.THRESHHOLD

		@export(float)
		@property
		def max(self):
				return self._max

		@threshholdlevel.setter
		def threshholdlevel(self, value):
				self.THRESHHOLD = value

		def _ready(self):
				try:
					self.streams = resolve_stream('type', 'EEG',5.0)
					if len(streams) == 0:
						self._error=True
					else:
						self.inlet = StreamInlet(self.streams[0])
						self.count=0.0
						self._max=0.0
						self.THRESHHOLD=40.0
						self._ready=True
				except:
					self._error=True

		def _process(self, delta):
			if(self._ready==True):
				self.count=self.count+1.0
							
				self.sample, self.timestamp = self.inlet.pull_sample()    
				self.sum+=self.sample[1]

				if(self.count==7.0):
					print(-1*((self.sum/7.0)))
					if(-1*((self.sum/7.0))>self.THRESHHOLD and -1*((self.sum/7.0))<100.0): 
						if(self._max<50.0):
							self._max=self._max+1.0
					else:
						if -1*((self.sum/7.0))>0.0 and self._max>0.0:
							#if(-1*((self.sum/20.0))>15.0):
							self._max=self._max-1.0
					self.sum=0 
					self.count=0				


class Helper:
		"""
		Other classes are considered helpers and cannot be called from outside
		Python. However they can be imported from another python module.
		"""

