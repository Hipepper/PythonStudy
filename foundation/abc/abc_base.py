import abc
import six


@six.add_metaclass(abc.ABCMeta)
class PluginBase(object):
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return
