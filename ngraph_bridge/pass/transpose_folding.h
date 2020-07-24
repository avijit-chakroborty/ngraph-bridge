/*******************************************************************************
 * Copyright 2017-2020 Intel Corporation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *******************************************************************************/
#pragma once

#include <fstream>
#include <ostream>
#include <sstream>

#include "ngraph/ngraph.hpp"
#include "ngraph/pass/pass.hpp"
#include "ngraph/pass/pass_util.hpp"

namespace tensorflow {
namespace ngraph_bridge {

// TODO: change to graph-rewrite pass
class TransposeFolding : public ngraph::pass::FunctionPass {
 public:
  TransposeFolding() {
    set_property(ngraph::pass::PassProperty::REQUIRE_STATIC_SHAPE, true);
  }
  bool run_on_function(std::shared_ptr<ngraph::Function> function) override;
};

}  // namespace ngraph_bridge
}  // namespace tensorflow
