# ==============================================================================
#  Copyright 2018-2020 Intel Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ==============================================================================
"""nGraph TensorFlow softplus test

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest

import numpy as np
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

from common import NgraphTest


class TestSoftplus(NgraphTest):

    def test_softplus(self):
        x = tf.compat.v1.placeholder(tf.float32, shape=(2, 3))
        y = tf.compat.v1.placeholder(tf.float32, shape=(2, 3))
        z = tf.compat.v1.placeholder(tf.float32, shape=(2, 3))

        a = x + y + z
        b = x + y + z
        c = a * b
        d = tf.nn.softplus(c)

        # input value and expected value
        x_np = np.full((2, 3), 1.0)
        y_np = np.full((2, 3), 1.0)
        z_np = np.full((2, 3), 1.0)

        sess_fn = lambda sess: sess.run((a, c, d),
                                        feed_dict={
                                            x: x_np,
                                            y: y_np,
                                            z: z_np
                                        })
        assert np.allclose(
            self.with_ngraph(sess_fn), self.without_ngraph(sess_fn))
